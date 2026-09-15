from flask import Flask

app = Flask(__name__)


@app.get("/health")
def health_check():
    return {
        "service": "healthcare-ai-data-science",
        "status": "healthy",
    }, 200


@app.errorhandler(404)
def resource_not_found(error):
    return {
        "error": "Resource not found",
        "status": 404,
    }, 404


if __name__ == "__main__":
    app.run()