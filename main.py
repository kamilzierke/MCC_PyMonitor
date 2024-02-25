from flask import Flask, render_template, jsonify
import socket
import struct
import pandas as pd
import threading

app = Flask(__name__)

# Setup UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.x', 8886)
sock.sendto(b"join", server_address)

# Initialize DataFrame with columns and cellIDs as index
columns = ['voltage', 'current', 'dischargeCap', 'chargeCap', 'esr', 'totalRuntime',
           'setDischargeCycles', 'completedDischargeCycles', 'temperature', 'maxVolt', 
           'storeVolt', 'minVolt', 'cellGroupID', 'status']
cell_ids = list(range(16))  # Assuming there are 16 cells (0-15)
battery_data = pd.DataFrame(index=cell_ids, columns=columns)
battery_data.index.name = 'cellID'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # Convert all bytes to strings to avoid serialization issues
    return jsonify(battery_data.applymap(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x).sort_index().to_dict(orient='index'))

def listen_for_data():
    while True:
        data, _ = sock.recvfrom(4096)
        if len(data) > 8:
            result = unpack_data(data)
            update_dataframe(result)

def unpack_data(data):
    format_string = '<I i i i i i f H H i i i i B 20s'
    size = struct.calcsize(format_string)
    unpacked_data = struct.unpack(format_string, data[:size])
    fields = ['cellID', 'voltage', 'current', 'dischargeCap', 'chargeCap', 'esr', 'totalRuntime',
              'setDischargeCycles', 'completedDischargeCycles', 'temperature', 'maxVolt', 'storeVolt',
              'minVolt', 'cellGroupID', 'status']
    return {fields[i]: unpacked_data[i] for i in range(len(fields))}

def update_dataframe(data_dict):
    cell_id = data_dict['cellID']
    for key, value in data_dict.items():
        if key != 'cellID':
            # Decode bytes to string if necessary
            if isinstance(value, bytes):
                value = value.decode('utf-8')
            battery_data.at[cell_id, key] = value

if __name__ == '__main__':
    threading.Thread(target=listen_for_data, daemon=True).start()
    app.run(debug=True, host='0.0.0.0', port=5000)
