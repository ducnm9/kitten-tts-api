# KittenTTS API

Powered by [KittenTTS GitHub repository](https://github.com/KittenML/KittenTTS)

KittenTTS API is a simple and easy-to-use Text-to-Speech (TTS) service.

## Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the application:**
   ```bash
   python app.py
   ```
3. **Run with Docker (optional):**
   ```bash
   docker build -t kitten-tts-api .
   docker run -p 8000:8000 kitten-tts-api
   ```

## Project Structure

- `app.py`: Main API source code.
- `requirements.txt`: List of required Python libraries.
- `Dockerfile`: Docker environment definition for the app.

## Contribution

All contributions are welcome! Please create a pull request or open an issue if you have ideas or find bugs.

## Quick Start & API Usage

After starting the application (with Python or Docker), you can test the API using `curl` or Postman.

### Supported Voices

You can choose one of the following voices when calling the API (default is `Bella`):

`['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']`

To get the list of available voices via API:

```bash
curl http://localhost:8000/voices
```

### Example: Synthesize with custom voice

```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, this is KittenTTS!", "voice": "Luna"}' \
     http://localhost:8000/synthesize
```

If you omit the `voice` field, the API will use the default voice Bella.

If you provide an invalid value for `voice`, the API will return an error and the list of valid voices.

Change the `text` and `voice` fields as you wish. The result will be an audio file.

**Note:** The audio file returned by the API is stored temporarily on the server and will be automatically deleted after 15 minutes to save resources. Please download the file immediately if you want to keep it.

## License

This project is licensed under the MIT License.
