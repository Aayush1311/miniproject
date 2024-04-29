from flask import Flask, render_template, request, jsonify
from stego import hide_text_in_image
from reverse_stego import extract_text_from_image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(' ')

@app.route('/encode', methods=['POST'])
def encode():
    image_path = request.form['image_path']
    text_file_path = request.form['text_file_path']
    output_image_path = request.form['output_image_path']
    key = request.form['key']

    try:
        result_image_path = hide_text_in_image(image_path, text_file_path, output_image_path, key)
        return jsonify({'success': True, 'result_image_path': result_image_path})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/decode', methods=['POST'])
def decode():
    image_path = request.form['image_path']
    key = request.form['key']
    output_text_path = request.form['output_text_path']

    try:
        extracted_text_path = extract_text_from_image(image_path, key, output_text_path)
        return jsonify({'success': True, 'extracted_text_path': extracted_text_path})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
