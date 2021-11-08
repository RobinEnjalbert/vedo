import vtk, sys

__all__ = []
_defs = ""
####################################################################################
####################################################################################
##### To generate documentation you must uncomment this line:
#from vedo.docs_defs import _substitutions_defs as _defs

# Then:
    # cd vedo/docs
    # pip install -r requirements.txt # optionally
    # make html

####################################################################################
####################################################################################


def tips():
    from vedo import colors, __version__
    msg  = " ==========================================================\n"
    msg += "| Press: i     print info about selected object            |\n"
    msg += "|        I     print the RGB color under the mouse         |\n"
    msg += "|        <-->  use arrows to reduce/increase opacity       |\n"
    msg += "|        w/s   toggle wireframe/surface style              |\n"
    msg += "|        p/P   change point size of vertices               |\n"
    msg += "|        l     toggle edges visibility                     |\n"
    msg += "|        x     toggle mesh visibility                      |\n"
    msg += "|        X     invoke a cutter widget tool                 |\n"
    msg += "|        1-2   change mesh color                           |\n"
    msg += "|        3     change mesh texture                         |\n"
    msg += "|        4     use data array as colors, if present        |\n"
    msg += "|        5-6   change background color(s)                  |\n"
    msg += "|        09+-  (on keypad) or +/- to cycle axes style      |\n"
    msg += "|        k     cycle available lighting styles             |\n"
    msg += "|        K     cycle available shading styles              |\n"
    msg += "|        A     toggle anti-aliasing                        |\n"
    msg += "|        D     toggle depth-peeling (for transparencies)   |\n"
    msg += "|        o/O   add/remove light to scene and rotate it     |\n"
    msg += "|        n     show surface mesh normals                   |\n"
    msg += "|        a     toggle interaction to Actor Mode            |\n"
    msg += "|        j     toggle interaction to Joystick Mode         |\n"
    msg += "|        r     reset camera position                       |\n"
    msg += "|        C     print current camera settings               |\n"
    msg += "|        S     save a screenshot                           |\n"
    msg += "|        E     export rendering window to numpy file       |\n"
    msg += "|        q     return control to python script             |\n"
    msg += "|        Esc   abort execution and exit python kernel      |\n"
    msg += "|----------------------------------------------------------|\n"
    msg += "| Mouse: Left-click    rotate scene / pick actors          |\n"
    msg += "|        Middle-click  pan scene                           |\n"
    msg += "|        Right-click   zoom scene in or out                |\n"
    msg += "|        Cntrl-click   rotate scene                        |\n"
    msg += "|----------------------------------------------------------|\n"
    msg += "| Check out documentation at:  https://vedo.embl.es        |\n"
    msg += " =========================================================="
    colors.printc(msg, dim=1)

    msg = " vedo " + __version__ + " "
    colors.printc(msg, invert=1, dim=1, end="")
    vtkVers = vtk.vtkVersion().GetVTKVersion()
    msg = "| vtk " + str(vtkVers)
    msg += " | python " + str(sys.version_info[0]) + "." + str(sys.version_info[1])
    colors.printc(msg, invert=0, dim=1)

####################################################################################
# example web page for X3D
x3d_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title> vedo with x3d </title>

  <!-- THESE ARE THE RELEVANT LINES: -->
  <script src='https://www.x3dom.org/download/x3dom.js'> </script>
  <link rel='stylesheet' type='text/css' href='https://www.x3dom.org/download/x3dom.css'/>

  <style>
     table, td, th { border: 1px solid black; background-color: powderblue;}
     table {width: 70%; border-collapse: collapse;}
     table th {width: 35%;}
  </style>
</head>

<body style="font-family: Verdana">
  <h1>Example html generated by vedo</h1>
  This example loads a 3D scene from file ~fileoutput generated by
  <a href="https://github.com/marcomusy/vedo">vedo</a>
  (see <a href="https://github.com/marcomusy/vedo/tree/master/examples/other/export_x3d.py">export_x3d.py</a>).
  <br><br>


  <!-- THESE ARE THE RELEVANT LINES: -->
  <x3d width='~widthpx' height='~heightpx'>
     <scene>
        <Inline url="~fileoutput"> </Inline>
     </scene>
  </x3d>

  <h3>Nothing shows up above this line?</h3>
  Enable your browser to load local files:
  <br><b>Firefox</b>: type <code>about:config</code> in the URL bar and
  change <code>privacy.file_unique_origin</code> from <code>True</code> to <code>False</code>
  <br><b>Chrome</b>: from terminal type:
  <code>google-chrome --enable-webgl --allow-file-access-from-files</code>
  (see <a href="https://cmatskas.com/interacting-with-local-data-files-using-chrome/">here</a>)

  <br>
  <h3>Controls:</h3>
  <h4><strong>Examine Mode (activate with key 'e'):</strong></h4>
  <table>
     <tbody>
        <tr class="even description">
           <th>Button</th>
           <th>Function</th>
        </tr>
        <tr>
           <td>Left Button / Left Button + Shift</td>
           <td>Rotate</td>
        </tr>
        <tr>
           <td>Mid Button / Left Button + Ctl</td>
           <td>Pan</td>
        </tr>
        <tr>
           <td>Right Button / Wheel / Left Button + Alt</td>
           <td>Zoom</td>
        </tr>
        <tr>
           <td>Left double click</td>
           <td>Set center of rotation</td>
        </tr>
     </tbody>
  </table>
  <h4><strong>Walk Mode (activate with key 'w'):</strong></h4>
  <table>
     <tbody>
        <tr class="even description">
           <th>Button</th>
           <th>Function</th>
        </tr>
        <tr>
           <td>Left Button</td>
           <td>Move forward</td>
        </tr>
        <tr>
           <td>Right Button</td>
           <td>Move backward</td>
        </tr>
     </tbody>
  </table>
  <h4><strong>Fly Mode (activate with key 'f'):</strong></h4>
  <table>
     <tbody>
        <tr class="even description">
           <th>Button</th>
           <th>Function</th>
        </tr>
        <tr>
           <td>Left Button</td>
           <td>Move forward</td>
        </tr>
        <tr>
           <td>Right Button</td>
           <td>Move backward</td>
        </tr>
     </tbody>
  </table>
  <h3>Non-interactive camera movement</h3>
  <table>
     <tbody>
        <tr class="even description">
           <th>Key</th>
           <th>Function</th>
        </tr>
        <tr>
           <td>r</td>
           <td>reset view</td>
        </tr>
        <tr>
           <td>a</td>
           <td>show all</td>
        </tr>
        <tr>
           <td>u</td>
           <td>upright</td>
        </tr>
     </tbody>
  </table>
</body>
</html>
"""
