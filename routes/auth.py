from flask import Flask, request, jsonify, Response
import json
from . import routes
import requests
from pprint import pprint

@routes.route("/auth", methods=['POST'])
def people():
	return Response('Hello World'), 200