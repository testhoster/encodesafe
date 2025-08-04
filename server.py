from flask import Flask, request, jsonify, send_from_directory
from encoder import encode_pipeline
from partialdecode import strip_wrappers
from fulldecoder import full_decode

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/encode', methods=['POST'])
def encode():
    data = request.json
    message = data.get('message')
    key = data.get('key')
    if not message or not key:
        return jsonify({'error': 'Missing input or key'}), 400

    encoded = encode_pipeline(message, key)
    raw_encrypted = encoded.replace('<', '').replace('>', '')
    hash_value = "SHA-256 hash not shown for security"
    return jsonify({
        'encoded': encoded,
        'encrypted': raw_encrypted,
        'hash': hash_value
    })

@app.route('/decode', methods=['POST'])
def decode():
    data = request.json
    wrapped = data.get('wrapped')
    key = data.get('key')

    if not wrapped:
        return jsonify({'result': '[Decode error: Missing input]'}), 400

    if not key:
        # partial decode
        try:
            partial = strip_wrappers(wrapped)
            return jsonify({'result': '[Partial Decode Result]:\n' + partial})
        except:
            return jsonify({'result': '[Decode error: Could not partially decode]'}), 400
    else:
        try:
            result = full_decode(wrapped, key)
            return jsonify({'result': '[Full Decode Result]:\n' + result})
        except:
            return jsonify({'result': '[Decode error: Invalid key or corrupted data]'}), 400

if __name__ == '__main__':
    app.run(debug=True)
