"""Simple Demo App"""

import io
import os
import datetime
import base64

from flask import Flask, Response, render_template
from flask_table import Table, Col

from datavisualizer.logger.log import LOGGER
from datavisualizer.config.config import AppConfig
from datavisualizer.storage.storage_factory import StorageFactory


app = Flask(__name__)
app.config.from_object(AppConfig)

if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    with app.app_context():
        env_storage = os.getenv('DATACOLLECTOR_STORAGE')
        if env_storage is None:
            env_storage = "mysql"
        STORAGE = StorageFactory.get_storage(env_storage)

class ShowTable(Table):
    classes = ['table', 'table-striped']
    id = Col('Id')
    topic = Col('Topic')
    message = Col('Message')

    def __init__(self, storage):
        self.storage = storage
        items = self.storage.read("SELECT * FROM data ORDER BY id DESC LIMIT 50")
        super(ShowTable, self).__init__(items)

    def handle_request(self):
        return render_template('index.html', title='Overview', table=self)


@app.route("/", methods=['GET', 'POST'])
def index():
    return ShowTable(STORAGE).handle_request()

@app.route("/alive", methods=['GET', 'POST'])
def alive():
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0')