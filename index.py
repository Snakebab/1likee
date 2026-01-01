from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/api/cron', methods=['GET'])
def long_running_task():
    # 1. DO YOUR WORK HERE
    print("Process started...")
    
    # Simulate a task (must finish within your plan's timeout limit)
    # If it takes longer than 10s (Hobby) or 300s (Pro), it will fail.
    result = "Data processed at " + time.ctime()

    # 2. RETURN A RESPONSE
    # This tells Vercel the function is done so it can reset for the next run.
    return jsonify({
        "status": "success",
        "processed": result
    }), 200

if __name__ == "__main__":
    app.run()
    