<h1>K-Means Color Segmentation Project</h1>
<p>This project applies the K-means clustering algorithm to perform color segmentation on an image.</p>

<h2>Files in the Project</h2>
<ul>
    <li><strong>main.py</strong>: Applies K-means clustering to an image for color segmentation.</li>
    <li><strong>super.png</strong>: Example input image used by <em>main.py</em>.</li>
    <li><strong>test1.txt</strong>: Output file containing numpy data of the image pixels.</li>
    <li><strong>pred1.txt</strong>: Output file containing predicted clusters for each pixel.</li>
    <li><strong>reconstructed_super.png</strong>: Output image file after color segmentation.</li>
</ul>

<h2>Libraries Used</h2>
<ul>
    <li><strong>numpy</strong>: Used for numerical computations and array operations.</li>
    <li><strong>PIL (Pillow)</strong>: Used for image processing tasks such as opening, saving, and manipulating images.</li>
</ul>

<h2>How to Run</h2>
<p>To run the <em>main.py</em> script, ensure you have Python installed along with the necessary libraries:</p>
<ul>
    <li>numpy: Install with <code>pip install numpy</code></li>
    <li>PIL: Install with <code>pip install Pillow</code></li>
</ul>
<p>Run the script using the following command:</p>
<pre><code>python main.py</code></pre>

<h2>Input</h2>
<p>The script reads an input image <em>super.png</em> located in the same directory. The image is loaded and processed for color segmentation.</p>
</br>
<img src="super.png" alt="Reconstructed Image" style="max-width: 100%;">

<h2>Output</h2>
<p>After running the script, several outputs are generated:</p>
<ul>
    <li><strong>test1.txt</strong>: Contains the numpy data of the image pixels.</li>
    <li><strong>pred1.txt</strong>: Contains the predicted cluster IDs for each pixel.</li>
    <li><strong>reconstructed_super.png</strong>: Shows the segmented image where each pixel is colored based on its cluster center.</li>
</ul>

<h2>Example Output</h2>
<p>Here is an example of the reconstructed image after applying K-means color segmentation:</p>
<img src="reconstructed_super.png" alt="Reconstructed Image" style="max-width: 100%;">

<p>For further details and explanations, refer to the comments within the source code of <em>main.py</em>.</p>
