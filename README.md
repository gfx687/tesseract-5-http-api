A basic HTTP API wrapper around [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

API:
- `POST /ocr`
	- IN: `multipart/form-data` with an `image` field
	- OUT: `{ "text": "extracted text" }`

Example:
```bash
curl --request POST \
	--url http://localhost:5000/ocr \
	--header 'content-type: multipart/form-data' \
	--form 'image=@C:\Users\Me\Downloads\test.jpg'
```
