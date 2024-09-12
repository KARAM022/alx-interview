<div class="col-xs-12 col-lg-10 contains-images">

      <h1 class="gap">
    0x07. Rotate 2D Matrix
    
  </h1>

  <div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[{&quot;id&quot;:17,&quot;value&quot;:&quot;Algorithm&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:19,&quot;value&quot;:&quot;Python&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;}]}" data-react-cache-id="tags/Tags-0"><div class="align-items-center d-flex flex-wrap gap-3 my-2"><span class="label label-primary" style="font-size: 14px;">Algorithm</span><span class="label label-primary" style="font-size: 14px;">Python</span></div></div>

  <div data-react-class="projects/ProjectMetadata" data-react-props="{&quot;metadata&quot;:{&quot;weight&quot;:1,&quot;correction&quot;:{&quot;released&quot;:true,&quot;auto_correction_available_at&quot;:&quot;2024-09-10T06:00:00.000+03:00&quot;,&quot;requires_auto_correction&quot;:true,&quot;requires_manual_correction&quot;:false},&quot;bpi&quot;:{&quot;current&quot;:true,&quot;started&quot;:false,&quot;in_second_deadline&quot;:false,&quot;starts_at&quot;:&quot;2024-09-09T06:00:00.000+03:00&quot;,&quot;ends_at&quot;:&quot;2024-09-13T06:00:00.000+03:00&quot;,&quot;second_deadline_at&quot;:&quot;2024-09-16T06:00:00.000+03:00&quot;}}}" data-react-cache-id="projects/ProjectMetadata-0"><ul class="list-group metadata" id="project-metadata"><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-gear fa-fw"></i> Weight: 1</li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-calendar fa-fw"></i> Project will start <span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2024-09-09 06:00 (GMT+03:00)"><span class="datetime">Sep 9, 2024 4:00 AM</span></span>, must end by <span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2024-09-13 06:00 (GMT+03:00)"><span class="datetime">Sep 13, 2024 4:00 AM</span></span></li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-check fa-fw"></i> Checker was released at <span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="2024-09-10 06:00 (GMT+03:00)"><span class="datetime">Sep 10, 2024 4:00 AM</span></span></li><li class="list-group-item"><i aria-hidden="true" class="fa-solid fa-square-check fa-fw"></i> An auto review will be launched at the deadline</li></ul></div>




    


    <div id="project_id" style="display: none" data-project-id="1220"></div>



      

      

      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <p>For the “0. Rotate 2D Matrix” project, you are tasked with implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Below are the key concepts and resources that you need to grasp in order to successfully complete this project.</p>

<h3>Concepts Needed:</h3>

<ol>
<li><p><strong>Matrix Representation in Python</strong>:</p>

<ul>
<li>Understanding how 2D matrices are represented using lists of lists in Python.</li>
<li>Accessing and modifying elements in a 2D matrix.</li>
</ul></li>
<li><p><strong>In-place Operations</strong>:</p>

<ul>
<li>Performing operations on data without creating a copy of the data structure.</li>
<li>The importance of minimizing space complexity by modifying the matrix in place.</li>
</ul></li>
<li><p><strong>Matrix Transposition</strong>:</p>

<ul>
<li>Understanding the concept of transposing a matrix (swapping rows and columns).</li>
<li>Implementing matrix transposition as a step in the rotation process.</li>
</ul></li>
<li><p><strong>Reversing Rows in a Matrix</strong>:</p>

<ul>
<li>Manipulating rows of a matrix by reversing their order as part of the rotation process.</li>
</ul></li>
<li><p><strong>Nested Loops</strong>:</p>

<ul>
<li>Using nested loops to iterate through 2D data structures like matrices.</li>
<li>Modifying elements within nested loops to achieve the desired rotation.</li>
</ul></li>
</ol>

<h3>Resources:</h3>

<ul>
<li><p><strong>Python Official Documentation</strong>:</p>

<ul>
<li><a href="/rltoken/eZc_ELGxUgkuc4kkE_fd7Q" title="Data Structures (list comprehensions, nested list comprehension)" target="_blank">Data Structures (list comprehensions, nested list comprehension)</a></li>
<li><a href="/rltoken/0ORj179giGhGe8jpcxBkXg" title="More on Lists" target="_blank">More on Lists</a></li>
</ul></li>
<li><p><strong>GeeksforGeeks Articles</strong>:</p>

<ul>
<li><a href="/rltoken/9T8w4mtiIIRDtfLSmEmrLA" title="Inplace rotate square matrix by 90 degrees" target="_blank">Inplace rotate square matrix by 90 degrees</a></li>
<li><a href="/rltoken/JdIFvtej2hMW-Wd9ABHMOA" title="Transpose a matrix in Single line in Python" target="_blank">Transpose a matrix in Single line in Python</a></li>
</ul></li>
<li><p><strong>TutorialsPoint</strong>:</p>

<ul>
<li><a href="/rltoken/rFmzUTpaLGqDXjGA6D9eYw" title="Python Lists" target="_blank">Python Lists</a> for basics of list manipulation in Python.</li>
</ul></li>
</ul>

<p>By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving their problem-solving and algorithmic thinking skills in Python.</p>

<h2>Additional Resources</h2>

<ul>
<li><a href="/rltoken/4GPWA9C2AJHtpdGxuIHEPA" title="Mock Technical Interview" target="_blank">Mock Technical Interview</a></li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.8.10)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.8.0)</li>
<li>You are not allowed to import any module</li>
<li>All modules and functions must be documented</li>
<li>All your files must be executable</li>
</ul>

  </div>
</div>


      

      

        
          <h2 class="gap">Tasks</h2>

    <div data-role="task11546" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-11546">
  <span id="user_id" data-id="434154"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Rotate 2D Matrix
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="434154"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Given an <code>n</code> x <code>n</code> 2D matrix, rotate it 90 degrees clockwise.</p>

<ul>
<li>Prototype: <code>def rotate_2d_matrix(matrix):</code></li>
<li>Do not return anything. The matrix must be edited <strong>in-place</strong>.</li>
<li>You can assume the matrix will have 2 dimensions and will not be empty.</li>
</ul>

<pre><code>jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
</code></pre>

  </div>

  <div class="list-group">
      <!-- LTI Resource -->

    <!-- Task Files -->

    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-interview</code></li>
            <li>Directory: <code>0x07-rotate_2d_matrix</code></li>
            <li>File: <code>0-rotate_2d_matrix.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="11546">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

      <button class="btn btn-default btn-sm check-your-task-11546-modal-button" data-task-id="11546" data-toggle="modal" data-target="#task-test-correction-11546-correction-modal" id="task-num-0-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11546}">
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11546-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "0. Rotate 2D Matrix"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="11546">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="11546">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="11546">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div>
    </div>
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:11546}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>




          <div class="modal fade" id="container-specs-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button><h4 class="modal-title">Recommended Sandbox</h4></div><div class="modal-body"><div data-react-class="user_containers/ContainerSpecs" data-react-props="{&quot;containerModelName&quot;:&quot;Sandbox&quot;,&quot;containerSpecs&quot;:[{&quot;available&quot;:true,&quot;description&quot;:&quot;\u003cp\u003eBasic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Foundations\u003c/p\u003e\n&quot;,&quot;id&quot;:39,&quot;name&quot;:&quot;Ubuntu 20.04&quot;,&quot;online&quot;:true}],&quot;containersLimit&quot;:2,&quot;csrfToken&quot;:&quot;puGG6D7D0xmRxgHQaCdByYXIWKJnrHjxUrEaNgMklnyp1oY2C1T92tG5vnu37HnwWqxilghvVQCBiSa0EJbVmg&quot;,&quot;startStatusURI&quot;:&quot;/user_containers/start_status.json&quot;,&quot;startURI&quot;:&quot;/user_containers/start.json&quot;}" data-react-cache-id="user_containers/ContainerSpecs-0"><div><div class="d-flex gap-4 sandboxes-filters"><a class="btn btn-outline-primary"><i aria-hidden="true" class="fa-solid fa-filter"></i><span class="ml-2">Running only</span></a><div class="align-items-center d-flex" style="position: relative; width: 100%;"><input class="form-control" placeholder="Search for an image ..." type="search" value=""></div></div><div class="mt-3"><h3>1 image<small class="ml-2">(0/2 Sandboxes spawned)</small></h3></div><div class="mt-3"><div class="panel panel-default"><div class="panel-body"><div class="align-items-center d-flex flex-wrap justify-content-between"><div><h3 class="mt-0"><i aria-hidden="true" class="fa-solid fa-terminal text-danger"></i><span class="ml-2">Ubuntu 20.04</span></h3><div class="mt-2 text-muted"><p>Basic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Foundations</p>
</div></div><div class="d-flex flex-wrap gap-5"><a class="btn btn-success"><i aria-hidden="true" class="fa-solid fa-play"></i><span class="ml-2">Run</span></a></div></div></div></div></div></div></div></div></div></div></div>

  </div>