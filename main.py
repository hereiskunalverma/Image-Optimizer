import streamlit as st
from PIL import Image
import time
import base64
timestr = time.strftime("%Y%m%d-%H%M%S")
import shutil
import os
def main(image):
	img=Image.open(image)
	value = st.slider("Select the optimize values : ",min_value=0, max_value=15,value=15)
	st.write("You have selected :", value)
	col1,col2=st.beta_columns(2)
	with col1:
		st.header("Original Image")
		st.image(image,caption=str(len(img.fp.read())/1000)+" KB",use_column_with=True)
	res="result.jpeg"
	img.save(res,optimize=True, quality=value)
	with col2:
		header="Result"
		st.header(header)
		st.image(res,caption=str(os.path.getsize(res)/1000)+" KB",use_column_with=True)
	if st.button("Save"):
		bs64 = 0
		with open(res,"rb") as img_file:
			bs64 = base64.b64encode(img_file.read()).decode();
		res_file = f"result_{timestr}"
		st.markdown("Downlaod file")
		href = f'<a href="data:file/jpeg;base64,{bs64}" download="{res_file}.jpg">Click Here!!</a>'
		st.markdown(href,unsafe_allow_html=True)
		# shutil.move(res,os.getcwd()+"\\Desktop\\"+res)
		# st.write("File Saved on Desktop")
	else:
		st.write("Not Saved!!!")
def pick():
	filename = st.file_uploader("Upload a file")
	if filename:
		main(filename)
	else:
		st.write("No File Uploaded!!!")
if __name__ == '__main__':
	st.title("Image Optimizer with Pillow")
	pick()
	st.markdown(
"""
			<style>
	a:link , a:visited{
	color: blue;
	background-color: transparent;
	text-decoration: underline;
	}

	a:hover,  a:active {
	color: red;
	background-color: transparent;
	text-decoration: underline;
	}

	.footer {
	position: fixed;
	left: 0;
	bottom: 0;
	width: 100%;
	background-color: white;
	color: black;
	text-align: center;
	}
	</style>
	<div class="footer">
	<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://hereiskunalverma.github.io/tlrc/index.html" target="_blank">Kunal Verma</a></p>
	</div>
"""
		,unsafe_allow_html=True)
