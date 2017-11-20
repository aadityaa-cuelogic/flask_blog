from flask import Blueprint, request, url_for, render_template, redirect
from . import app

@app.route('/')
def index():
	return "Hello World"