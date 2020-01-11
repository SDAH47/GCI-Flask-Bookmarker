from flask import Flask, render_template, send_from_directory
import os

app = Flask( __name__, template_folder = os.path.dirname( os.path.realpath( __file__ ) ) )

@app.route( '/' )

def index(): 
	return render_template( 'index.html' )

# Resources
@app.route( '/css/<path:path>' )

def send_css( path ): 
	return send_from_directory( 'css', path )

@app.route( '/js/<path:path>' )

def send_js( path ): 
	return send_from_directory( 'js', path )

@app.route( '/images/<path:path>' )

def send_images( path ): 
	return send_from_directory( 'images', path )

if __name__ == '__main__': 
	app.run( debug= True )