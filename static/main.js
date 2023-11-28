/***********************************************
                DOCUMENT ELEMENTS                   
***********************************************/
// - User Input
const memoryBlocksInput = document.getElementById('memory-blocks-input');
const testCaseInput = document.getElementById('test-case-input');

// - Buttons
const startSimulation = document.getElementById('start-simulation');
const playTraceback = document.getElementById('play-traceback');
const pauseTraceback = document.getElementById('pause-traceback');
const continueTraceback = document.getElementById('continue-traceback');
const resetTraceback = document.getElementById('reset-traceback');
const resetContainer = document.getElementById('reset-container');
const tracebackContainer = document.getElementById('traceback-container');
const stateButtons = document.querySelectorAll('.state-button');
const previousStateButton = document.getElementById('previous-state');
const nextStateButton = document.getElementById('next-state');

// - Titles and Sub-titles
const cacheIterationCounter = document.getElementById('cache-iteration-counter');
const cacheOutputDetails = document.getElementById('cache-output-details');
const cacheTestCaseType = document.getElementById('cache-test-case-type');

// - Cache Output Details
const memoryAccessCountLabel = document.getElementById('memory-access-count');
const memoryAccessCount = document.getElementById('memory-access-count');
const cacheHitCountLabel = document.getElementById('cache-hit-count');
const cacheMissCountLabel = document.getElementById('cache-miss-count');
const cacheHitRateLabel = document.getElementById('cache-hit-rate');
const cacheMissRateLabel = document.getElementById('cache-miss-rate');
const averageAccessTime = document.getElementById('average-access-time');
const totalAccessTime = document.getElementById('total-access-time');

// - Text Log
const textLogContent = document.getElementById('text-log-content');
const nextPageButton = document.getElementById('next-page-button');
const previousPageButton = document.getElementById('previous-page-button');

/***********************************************
                    VARIABLES                   
***********************************************/
// - Cache Simulation Details
var sequence;

// - Cache Memory Retracing
var cacheDetails;
var cacheAccessLog;
var finalSnapshot;
var maxIteration;
var currentIteration;
var isPaused = false;

// - Cache Memory Text Log
var cacheTextLog;
var cacheTagLog;
var spansPerPage = 25;
var currentPage;
var maxPage;

/***********************************************
                 FETCH REQUESTS             
***********************************************/
async function fetchPost( URL, formData ) {
    var response = await fetch( URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify( formData ),
    }); 
    return response;
}

/***********************************************
                SIMULATION BUTTON           
***********************************************/
startSimulation.addEventListener( "click", async function() {
    resetTracebackButtonStyles();

    if( memoryBlocksInput.value === '' ) {
        tracebackContainer.setAttribute('style', 'display: none;');
        return; // - Must input memory blocks number
    }

    try {
        // - Prepare form data and send a POST request
        const simulationFormData = {
            numBlocks: parseInt(memoryBlocksInput.value),
            testCase: parseInt(testCaseInput.value, 10)
        };

        const response = await fetchPost( '/simulation', simulationFormData );
        if( response.status !== 200 ) {
            return; // - Fetch failed
        }
        
        // - For cache memory simulation details
        const parsedResponse = await response.json();
        sequence = parsedResponse.sequence;
        cacheDetails = parsedResponse.cacheDetails;

        // - For cache memory retracing
        cacheAccessLog = parsedResponse.cacheAccessLog;
        finalSnapshot = parsedResponse.finalSnapshot;

        // - For cache memory text log
        cacheTextLog = parsedResponse.cacheTextLog;
        cacheTagLog = parsedResponse.cacheTagLog;

        // - Update cache details
        updateCacheOutputDetails(cacheDetails);
        updateCacheMemory(finalSnapshot);
        updateCacheTestCaseType(testCaseInput.value);
        tracebackContainer.setAttribute('style', 'display: visible;');

        // - Update text log
        currentPage = 1;
        maxPage = Math.ceil(maxIteration/spansPerPage);
        updateTextLog();

    } catch( error ) {
        console.log( error );
    }
});

function updateCacheOutputDetails( cacheDetails ) {
    maxIteration = cacheDetails[0];
    memoryAccessCountLabel.textContent = cacheDetails[0];
    cacheHitCountLabel.textContent = cacheDetails[1];
    cacheMissCountLabel.textContent = cacheDetails[2];
    cacheHitRateLabel.textContent = (cacheDetails[3]*100).toFixed(2) + "%";
    cacheMissRateLabel.textContent = (cacheDetails[4]*100).toFixed(2) + "%";
    averageAccessTime.textContent = cacheDetails[5] + "ns";
    totalAccessTime.textContent = cacheDetails[6] + "ns";
}

function updateCacheMemory( snapshot ) {
    var cacheBlocks = document.querySelectorAll('[id^="cache-block-"]');

    cacheBlocks.forEach(function(cacheBlock,index) {
        var item = snapshot[index];
        cacheBlock.textContent = item.data;
    });
    
    cacheIterationCounter.textContent = `(${maxIteration}/${maxIteration})`;
}

function updateCacheTestCaseType( testCase ) {
    message = "[FA LRU: "

    switch( testCase ) {
        case "0": message += "Sequential Test Case]"; break;
        case "1": message += "Random Test Case]"; break;
        case "2": message += "Mid-Repeat Test Case]"; break;
        default: message = ""; break;
    }

    cacheTestCaseType.textContent = message;
}

/***********************************************
           CACHEBLOCK ANIMATION FUNCTIONS           
***********************************************/
function startCacheAnimation() {
    async function updateAndDelay() {
        if( !isPaused && currentIteration < maxIteration ) {
            await updateCacheBlock(currentIteration);
            currentIteration++;
            setTimeout(updateAndDelay, 100);
        }
    }
    updateAndDelay();
}

function resetTracebackButtonStyles() {
    isPaused = true;
    resetCacheBlocksStyle();

    // - Reset button visibility to default
    playTraceback.setAttribute('style', 'display: visible;');
    pauseTraceback.setAttribute('style', 'display: none;');
    continueTraceback.setAttribute('style', 'display: none;');
    resetContainer.setAttribute('style', 'display: none;');    
    stateButtons.forEach(function(button) {
        button.style.display = 'none';
    });
}

// - Remove "selected" style from previous cacheblocks
function resetCacheBlocksStyle() {
    var cacheBlocks = document.querySelectorAll('[id^="cache-block-"]');
    cacheBlocks.forEach(function (block) {
        block.classList.remove('selected');
    });
}

function clearCacheMemory() {
    var cacheBlocks = document.querySelectorAll('[id^="cache-block-"]');

    cacheBlocks.forEach(function(cacheBlock) {
        cacheBlock.textContent = '';
    });
}

async function updateCacheBlock( iteration ) {
    resetCacheBlocksStyle();

    // - Find the current cacheblock and add "selected" style
    var currentBlock = iteration % 32;
    var cacheBlockData = cacheAccessLog[iteration].data;
    var targetCacheBlockId = "cache-block-" + currentBlock;
    var cacheBlock = document.getElementById(targetCacheBlockId);
    cacheBlock.textContent = cacheBlockData;
    cacheBlock.classList.add('selected');

    // - Update iteration counter
    cacheIterationCounter.textContent = `(${currentIteration+1}/${maxIteration})`;
}

/***********************************************
           CACHEBLOCK ANIMATION BUTTONS           
***********************************************/
playTraceback.addEventListener( "click", async function() {
    clearCacheMemory();
    currentIteration = 0;
    isPaused = false;

    // - Hide play button and display pause button
    playTraceback.setAttribute('style', 'display: none;');
    pauseTraceback.setAttribute('style', 'display: visible;');
    resetContainer.setAttribute('style', 'display: visible;');

    // - Hide state buttons
    stateButtons.forEach(function(button) {
        button.style.display = 'none';
    });

    startCacheAnimation();
});

pauseTraceback.addEventListener( "click", async function() {
    isPaused = true;

    // - Hide pause button and display pause button
    pauseTraceback.setAttribute('style', 'display: none;');
    continueTraceback.setAttribute('style', 'display: visible;');

    // - Display state buttons
    stateButtons.forEach(function(button) {
        button.style.display = 'block';
    });
});

continueTraceback.addEventListener( "click", async function() {
    isPaused = false;

    // - Hide pause button and display pause button
    continueTraceback.setAttribute('style', 'display: none;');
    pauseTraceback.setAttribute('style', 'display: visible;');

    startCacheAnimation();
});

nextStateButton.addEventListener( "click", async function() {
    if( currentIteration > maxIteration ) {
        return;
    }

    isPaused = false;
    await updateCacheBlock(currentIteration);
    currentIteration++;
    cacheIterationCounter.textContent = `(${currentIteration}/${maxIteration})`;
});

previousStateButton.addEventListener( "click", async function() {
    if( currentIteration <= 0 ) {
        return;
    }

    isPaused = false;
    clearCacheMemory();
    currentIteration--;
    for( i = 0; i < currentIteration; i++ ) {
        await updateCacheBlock(i);
    }
    cacheIterationCounter.textContent = `(${currentIteration}/${maxIteration})`;
});

resetTraceback.addEventListener( "click", async function() {
    resetTracebackButtonStyles();

    // - Restore to final snapshot
    updateCacheMemory(finalSnapshot);
    cacheIterationCounter.textContent = `(${maxIteration}/${maxIteration})`;
});

/***********************************************
              TEXT LOG FUNCTIONS         
***********************************************/
nextPageButton.addEventListener( "click", async function() {
    var newPage = currentPage + 1;

    console.log( "Current = " + currentPage + " | New = " + newPage + "\n" );
    console.log( "Max = " + maxPage );

    if( newPage > 0 && newPage <= maxPage ) {
        currentPage = newPage;
        updateTextLog();
    }
});

previousPageButton.addEventListener( "click", async function() {
    var newPage = currentPage - 1;

    console.log( "Current = " + currentPage + " | New = " + newPage + "\n" );
    console.log( "Max = " + maxPage );
    
    if( newPage > 0 && newPage <= maxPage ) {
        currentPage = newPage;
        updateTextLog();
    }
});

function updateTextLog() {    
    var start = (currentPage - 1) * spansPerPage;   
    var end = start + spansPerPage;
    
    console.log( "Start: " + start + " | End: " + end + "\n" );

    // - Clear container
    textLogContent.innerHTML = '';

    // - Create spans to container
    for( var i = start; i < end; i++ ) {
        const span = document.createElement('span');
        span.textContent = cacheTextLog[i].textLog;
    
        switch( cacheTagLog[i] ) {
            case 1: span.classList.add('cache-hit'); break;
            case 2: span.classList.add('cache-empty'); break;
            case 3: span.classList.add('cache-lru'); break;
            default: break;
        }
    
        textLogContent.appendChild(span);
    }
}