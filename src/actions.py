import io

from flask import Blueprint, current_app, jsonify, request, send_file

from src.bucket import get_bucket

bucket_actions_bp = Blueprint("bucket_actions", __name__)


@bucket_actions_bp.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    try:
        file_name = file.filename
        blob = get_bucket().blob(file_name)
        blob.upload_from_file(file)
        return jsonify({"status": "ok", "file_name": file_name})
    except Exception as e:
        error_message = f"Error uploading file: {e}"
        current_app.logger.error(error_message)
        return jsonify({"status": "error", "message": error_message})


@bucket_actions_bp.route("/download", methods=["GET"])
def download():
    file_name = request.args.get("file_name", "")
    if not file_name:
        return jsonify({"status": "error", "message": "File name is required"}), 400

    try:
        blob = get_bucket().blob(file_name)
        content = blob.download_as_bytes()
        return send_file(
            io.BytesIO(content),
            mimetype="application/octet-stream",
            as_attachment=True,
            download_name=file_name,
        )
    except Exception as e:
        error_message = f"Error downloading file: {e}"
        current_app.logger.error(error_message)
        return jsonify({"status": "error", "message": error_message}), 500


@bucket_actions_bp.route("/delete", methods=["DELETE"])
def delete():
    file_name = request.args.get("file_name", "")

    if not file_name:
        return jsonify({"status": "error", "message": "File name is required"}), 400

    try:
        blob = get_bucket().blob(file_name)
        blob.delete()
        return jsonify({"status": "ok", "message": "File deleted successfully"})
    except Exception as e:
        error_message = f"Error deleting file: {e}"
        current_app.logger.error(error_message)
        return jsonify({"status": "error", "message": error_message}), 500
