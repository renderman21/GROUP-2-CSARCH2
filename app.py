from flask import Flask, render_template, jsonify, request
from python.sequence import Sequence
from python.cache import CacheMemory, CacheBlock

'''
    Setting Up Flask:
        python -m venv venv
        .\venv\Scripts\activate

    For VSC:
        ctrl + shift + p pick "Choose Interpreter"
        pick one with .\venv

    Terminal:
        python -m pip install --upgrade pip
        python -m pip install flask

    Run:
        flask --app app.py --debug run
'''

app = Flask(__name__)

# Main page
@app.route("/")
def home():
    return render_template('main.html')

# Cache Simulation
@app.route('/simulation', methods=['POST'])
def simulate():    
    try:
        # Parse number of memory blocks and test case
        data = request.get_json()
        numBlocks = data['numBlocks']
        testCase = data['testCase']
        
        # Generate sequence
        sequence = Sequence(numBlocks)
        list = sequence.initSequence(testCase)

        # Generate cache memory 
        cacheSize = 32
        cacheMemory = CacheMemory(cacheSize)

        # Start simulation
        cacheMemory.accessMemory(list)

        # For cache memory simulation details
        memoryAccessCount = cacheMemory.iteration
        cacheHitCount = cacheMemory.getCacheHitCount()
        cacheMissCount = cacheMemory.getCacheMissCount()
        cacheHitRate = cacheMemory.getCacheHitRate()
        cacheMissRate = cacheMemory.getCacheMissRate()
        averageMAT = cacheMemory.getAverageMAT()
        totalMAT = cacheMemory.getTotalMAT()

        # For cache memory retracing
        cacheAccessLog = cacheMemory.cacheAccessLog
        finalSnapshot = cacheMemory.getFinalSnapshot()

        # For cache memory text log
        cacheTextLog = cacheMemory.cacheTextLog
        cacheTagLog = cacheMemory.cacheTagLog

        cacheDetails = [
            memoryAccessCount,
            cacheHitCount,
            cacheMissCount,
            cacheHitRate,
            cacheMissRate,
            averageMAT,
            totalMAT
        ]

        # Convert cacheAccessLog, finalSnapshot, cacheTextLog to JSON
        jsonAccessLog = [{ "number": log.number, "data": log.data } for log in cacheAccessLog ]
        jsonSnapshot = [{ "number": log.number, "data": log.data } for log in finalSnapshot ]
        jsonTextLog = [{ "textLog": log } for log in cacheTextLog ]

        response = {
            "sequence": list,
            "cacheDetails": cacheDetails,
            "cacheAccessLog": jsonAccessLog,
            "finalSnapshot": jsonSnapshot,
            "cacheTextLog": jsonTextLog,
            "cacheTagLog": cacheTagLog
        }

        return jsonify(response), 200
    except (KeyError, ValueError) as e:
        return jsonify({ "error": f"Invalid input data; {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)