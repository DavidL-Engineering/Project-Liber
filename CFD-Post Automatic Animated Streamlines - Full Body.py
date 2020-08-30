# encoding: utf-8
# 2020 R1
# Written by BOT Yokel
# WARNING: This script will not work if you have changed the order of the modules (e.g. created 5 modules and deleted any of modules 1-4)
SetScriptVersion(Version="20.1.164")

# Paste the filepaths below to be the parent folder you would like all data to be saved in
# WARNING: This program cannot make folders! Please ensure that the file path exists
# Change all backslashes to forward slashes!
# e.g. filepaths = ["C:/Users/david/Documents/1_(SSD)_Important_Things/Work/Ansys Work/David/Test Aerobody 7 Refined/Sim 14/Media Files"]
filepaths = [
"FILEPATH_1",
"FILEPATH_2"
]

# Paste the name of the Fluent modules below
# e.g. modules = ["Wheelbase65 Aero7_Jet_Engine_Sim14_Refined"]
modules = [
"MODULE_1",
"MODULE_2"
]

if len(filepaths) == 1 and len(modules) == 1:
    queue = 1
else:
    queue = len(filepaths)

# Will run every time when lists are non-empty
if queue:
  system1 = GetSystem(Name="Post")
  results1 = system1.GetContainer(ComponentName="Results")
  results1.Edit()
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >hide /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /DATA READER/CASE:Case {}/BOUNDARY:car, view=/VIEW:View 1""".format(modules[0]))
  results1.SendCommand(Command="""VIEW:View 1
    Camera Mode = User Specified
    CAMERA:
      Option = Pivot Point and Quaternion
      Pivot Point = 2.45395, 0, 0.584167
      Scale = 0.656586
      Pan = 0.0997342, -0.360136
      Rotation Quaternion = -0.555856, 0.2474, 0.348336, 0.713069
      
    END

  END

  VIEW:View 1
    Light Angle = 101.003, 125.876
  END

  > update
  > autolegend plot=/ISOSURFACE:Isosurface Y 0, view=VIEW:View 1""")
  results1.SendCommand(Command="""ISOSURFACE:Isosurface Y 0
  Apply Instancing Transform = On
  Apply Texture = Off
  Blend Texture = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Colour = 0, 0, 0
  Line Colour Mode = Default
  Line Width = 1
  Max = 0.0 [m s^-1]
  Min = 0.0 [m s^-1]
  Range = Global
  Render Edge Angle = 0 [degree]
  Specular Lighting = On
  Surface Drawing = Smooth Shading
  Texture Angle = 0
  Texture Direction = 0 , 1 , 0 
  Texture File =  
  Texture Material = Metal
  Texture Position = 0 , 0 
  Texture Scale = 1
  Texture Type = Predefined
  Tile Texture = Off
  Transform Texture = Off
  Transparency = 0.0
  Value = 0.0 [m]
  Variable = Y
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /ISOSURFACE:Isosurface Y 0, view=/VIEW:View 1""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >hide /ISOSURFACE:Isosurface Y 0, view=/VIEW:View 1""")
  results1.SendCommand(Command="> autolegend plot=/ISOSURFACE:Isosurface Pos Y 40, view=VIEW:View 1")
  results1.SendCommand(Command="""ISOSURFACE:Isosurface Pos Y 40
  Apply Instancing Transform = On
  Apply Texture = Off
  Blend Texture = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Colour = 0, 0, 0
  Line Colour Mode = Default
  Line Width = 1
  Max = 0.0 [m s^-1]
  Min = 0.0 [m s^-1]
  Range = Global
  Render Edge Angle = 0 [degree]
  Specular Lighting = On
  Surface Drawing = Smooth Shading
  Texture Angle = 0
  Texture Direction = 0 , 1 , 0 
  Texture File =  
  Texture Material = Metal
  Texture Position = 0 , 0 
  Texture Scale = 1
  Texture Type = Predefined
  Tile Texture = Off
  Transform Texture = Off
  Transparency = 0.0
  Value = 0.4 [m]
  Variable = Y
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /ISOSURFACE:Isosurface Pos Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >hide /ISOSURFACE:Isosurface Pos Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="> autolegend plot=/ISOSURFACE:Isosurface Neg Y 40, view=VIEW:View 1")
  results1.SendCommand(Command="""ISOSURFACE:Isosurface Neg Y 40
  Apply Instancing Transform = On
  Apply Texture = Off
  Blend Texture = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Colour = 0, 0, 0
  Line Colour Mode = Default
  Line Width = 1
  Max = 0.0 [m s^-1]
  Min = 0.0 [m s^-1]
  Range = Global
  Render Edge Angle = 0 [degree]
  Specular Lighting = On
  Surface Drawing = Smooth Shading
  Texture Angle = 0
  Texture Direction = 0 , 1 , 0 
  Texture File =  
  Texture Material = Metal
  Texture Position = 0 , 0 
  Texture Scale = 1
  Texture Type = Predefined
  Tile Texture = Off
  Transform Texture = Off
  Transparency = 0.0
  Value = -0.4 [m]
  Variable = Y
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /ISOSURFACE:Isosurface Neg Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >hide /ISOSURFACE:Isosurface Neg Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Streamline Y 0, view=VIEW:View 1")
  results1.SendCommand(Command="""STREAMLINE:Streamline Y 0
  Absolute Tolerance = 0.0 [m]
  Apply Instancing Transform = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Cross Periodics = On
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Draw Streams = On
  Draw Symbols = Off
  Grid Tolerance = 0.01
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Width = 1
  Location List = /ISOSURFACE:Isosurface Y 0
  Locator Sampling Method = Vertex
  Max = 0.0 [m s^-1]
  Maximum Number of Items = 150
  Min = 0.0 [m s^-1]
  Number of Samples = 500
  Number of Sides = 8
  Range = Global
  Reduction Factor = 1.0
  Reduction or Max Number = Max Number
  Sample Spacing = 0.1
  Sampling Aspect Ratio = 1
  Sampling Grid Angle = 0 [degree]
  Seed Point Type = Equally Spaced Samples
  Simplify Geometry = Off
  Specular Lighting = On
  Stream Drawing Mode = Line
  Stream Initial Direction = 0 , 0 , 0 
  Stream Size = 1.0
  Stream Symbol = Ball
  Streamline Direction = Forward and Backward
  Streamline Maximum Periods = 20
  Streamline Maximum Segments = 10000
  Streamline Maximum Time = 0.0 [s]
  Streamline Type = 3D Streamline
  Streamline Width = 2
  Surface Drawing = Smooth Shading
  Surface Streamline Direction = Forward and Backward
  Symbol Size = 1.0
  Symbol Start Time = 10.0 [s]
  Symbol Stop Time = -10.0 [s]
  Symbol Time Interval = 1.0 [s]
  Tolerance Mode = Grid Relative
  Transparency = 0.0
  Variable = Velocity
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /STREAMLINE:Streamline Y 0, view=/VIEW:View 1""")
  results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Streamline Pos Y 40, view=VIEW:View 1")
  results1.SendCommand(Command="""STREAMLINE:Streamline Pos Y 40
  Absolute Tolerance = 0.0 [m]
  Apply Instancing Transform = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Cross Periodics = On
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Draw Streams = On
  Draw Symbols = Off
  Grid Tolerance = 0.01
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Width = 1
  Location List = /ISOSURFACE:Isosurface Pos Y 40
  Locator Sampling Method = Vertex
  Max = 0.0 [m s^-1]
  Maximum Number of Items = 150
  Min = 0.0 [m s^-1]
  Number of Samples = 500
  Number of Sides = 8
  Range = Global
  Reduction Factor = 1.0
  Reduction or Max Number = Max Number
  Sample Spacing = 0.1
  Sampling Aspect Ratio = 1
  Sampling Grid Angle = 0 [degree]
  Seed Point Type = Equally Spaced Samples
  Simplify Geometry = Off
  Specular Lighting = On
  Stream Drawing Mode = Line
  Stream Initial Direction = 0 , 0 , 0 
  Stream Size = 1.0
  Stream Symbol = Ball
  Streamline Direction = Forward and Backward
  Streamline Maximum Periods = 20
  Streamline Maximum Segments = 10000
  Streamline Maximum Time = 0.0 [s]
  Streamline Type = 3D Streamline
  Streamline Width = 2
  Surface Drawing = Smooth Shading
  Surface Streamline Direction = Forward and Backward
  Symbol Size = 1.0
  Symbol Start Time = 10.0 [s]
  Symbol Stop Time = -10.0 [s]
  Symbol Time Interval = 1.0 [s]
  Tolerance Mode = Grid Relative
  Transparency = 0.0
  Variable = Velocity
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /STREAMLINE:Streamline Pos Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Streamline Neg Y 40, view=VIEW:View 1")
  results1.SendCommand(Command="""STREAMLINE:Streamline Neg Y 40
  Absolute Tolerance = 0.0 [m]
  Apply Instancing Transform = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Cross Periodics = On
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Draw Streams = On
  Draw Symbols = Off
  Grid Tolerance = 0.01
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Width = 1
  Location List = /ISOSURFACE:Isosurface Neg Y 40
  Locator Sampling Method = Vertex
  Max = 0.0 [m s^-1]
  Maximum Number of Items = 150
  Min = 0.0 [m s^-1]
  Number of Samples = 500
  Number of Sides = 8
  Range = Global
  Reduction Factor = 1.0
  Reduction or Max Number = Max Number
  Sample Spacing = 0.1
  Sampling Aspect Ratio = 1
  Sampling Grid Angle = 0 [degree]
  Seed Point Type = Equally Spaced Samples
  Simplify Geometry = Off
  Specular Lighting = On
  Stream Drawing Mode = Line
  Stream Initial Direction = 0 , 0 , 0 
  Stream Size = 1.0
  Stream Symbol = Ball
  Streamline Direction = Forward and Backward
  Streamline Maximum Periods = 20
  Streamline Maximum Segments = 10000
  Streamline Maximum Time = 0.0 [s]
  Streamline Type = 3D Streamline
  Streamline Width = 2
  Surface Drawing = Smooth Shading
  Surface Streamline Direction = Forward and Backward
  Symbol Size = 1.0
  Symbol Start Time = 10.0 [s]
  Symbol Stop Time = -10.0 [s]
  Symbol Time Interval = 1.0 [s]
  Tolerance Mode = Grid Relative
  Transparency = 0.0
  Variable = Velocity
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /STREAMLINE:Streamline Neg Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="""VIEW:View 1
  Camera Mode = User Specified
  CAMERA:
  Option = Pivot Point and Quaternion
  Pivot Point = 2.51148, 0.64251, 0.68061
  Scale = 0.803174
  Pan = 2.19897, -0.011249
  Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17

  END

  END

  > update
  ANIMATION:ANIMATION
  QAnim MPEG Filename = {}/Trailing Edge and Wake Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4

  END""".format(filepaths[0]))
  results1.SendCommand(Command="""ANIMATION:
  Animation Bit Rate = 5152000
  Animation Frame Rate = 24
  Animation Quality = Highest
  Animation Speed Factor = 2
  Antialiasing = On
  Drop Last MPEG Frame = Off
  Hardcopy Tolerance = 0.0001
  Intermediate File Format = jpg
  Keep Intermediate Files = Off
  MPEG Height = 1080
  MPEG Scale = 100
  MPEG Size = 1080p
  MPEG Width = 1920
  Output Directory = .
  Output to User Directory = Off
  QAnim Override Symbol = On
  QAnim Symbol Size = 0.05
  QAnim Symbol Spacing = 0.3
  QAnim Symbol Type = Ball
  Screen Capture = Off
  Speed Adjustment Selection = Normal
  Speed Scaling Method = Distribute Frames Smoothly
  Timestep Interpolation Method = Timestep
  Variable Bit Rate = On
  White Background = Off
  END""")
  results1.SendCommand(Command="""ANIMATION: ANIMATION
  QAnim Object List = /STREAMLINE:Streamline Neg Y 40,/STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
  QAnim Frames = 100
  QAnim MPEG Filename = {}/Trailing Edge and Wake Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4
  END
  >animate quickAnimate""".format(filepaths[0]))
  results1.SendCommand(Command="""VIEW:View 1
    Camera Mode = User Specified
    CAMERA:
      Option = Pivot Point and Quaternion
      Pivot Point = 4.4939, 0.459533, 0.511379
      Scale = 0.624333
      Pan = 0.756583, -0.215757
      Rotation Quaternion = -3.72529e-09, 0.707107, 0.707107, -3.72529e-09
      
    END

  END

  > update
  QAnim MPEG Filename = {}/Trailing Edge and Wake 2 Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4

  END""".format(filepaths[0]))
  results1.SendCommand(Command="""ANIMATION: ANIMATION
  QAnim Object List = /STREAMLINE:Streamline Neg Y 40,/STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
  QAnim Frames = 100
  QAnim MPEG Filename = {}/Trailing Edge and Wake 2 Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4
  END
  >animate quickAnimate""".format(filepaths[0]))
  results1.SendCommand(Command="""VIEW:View 1
    Camera Mode = User Specified
    CAMERA:
      Option = Pivot Point and Quaternion
      Pivot Point = 4.4939, 0.459533, 0.511379
      Scale = 0.860138
      Pan = -1.27971, -0.419625
      Rotation Quaternion = -3.72529e-09, 0.707107, 0.707107, -3.72529e-09
      
    END

  END

  > update
  ANIMATION:ANIMATION
  QAnim MPEG Filename = {}/Canopy Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4

  END""".format(filepaths[0]))
  results1.SendCommand(Command="""ANIMATION: ANIMATION
  QAnim Object List = /STREAMLINE:Streamline Neg Y 40,/STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
  QAnim Frames = 100
  QAnim MPEG Filename = {}/Canopy Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4
  END
  >animate quickAnimate""".format(filepaths[0]))
  results1.SendCommand(Command="""VIEW:View 1
    Camera Mode = User Specified
    CAMERA:
      Option = Pivot Point and Quaternion
      Pivot Point = 3.23676, 0.504839, 0.995587
      Scale = 0.289498
      Pan = -0.24374, -1.06636
      Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17
      
    END

  END

  > update
  ANIMATION:ANIMATION
  QAnim MPEG Filename = {}/Right Side Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4

  END""".format(filepaths[0]))
  results1.SendCommand(Command="""ANIMATION: ANIMATION
  QAnim Object List = /STREAMLINE:Streamline Neg Y 40,/STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
  QAnim Frames = 100
  QAnim MPEG Filename = {}/Right Side Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4
  END
  >animate quickAnimate""".format(filepaths[0]))
  results1.Exit()

for num in range(1,queue):
  system1 = GetSystem(Name="Post")
  results1 = system1.GetContainer(ComponentName="Results")
  results1.Edit()
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >hide /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /DATA READER/CASE:Case {}/BOUNDARY:car, view=/VIEW:View 1""".format(modules[num]))
  results1.SendCommand(Command="""VIEW:View 1
    Camera Mode = User Specified
    CAMERA:
      Option = Pivot Point and Quaternion
      Pivot Point = 2.45395, 0, 0.584167
      Scale = 0.656586
      Pan = 0.0997342, -0.360136
      Rotation Quaternion = -0.555856, 0.2474, 0.348336, 0.713069
      
    END

  END

  VIEW:View 1
    Light Angle = 101.003, 125.876
  END

  > update
  > autolegend plot=/ISOSURFACE:Isosurface Y 0, view=VIEW:View 1""")
  results1.SendCommand(Command="""ISOSURFACE:Isosurface Y 0
  Apply Instancing Transform = On
  Apply Texture = Off
  Blend Texture = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Colour = 0, 0, 0
  Line Colour Mode = Default
  Line Width = 1
  Max = 0.0 [m s^-1]
  Min = 0.0 [m s^-1]
  Range = Global
  Render Edge Angle = 0 [degree]
  Specular Lighting = On
  Surface Drawing = Smooth Shading
  Texture Angle = 0
  Texture Direction = 0 , 1 , 0 
  Texture File =  
  Texture Material = Metal
  Texture Position = 0 , 0 
  Texture Scale = 1
  Texture Type = Predefined
  Tile Texture = Off
  Transform Texture = Off
  Transparency = 0.0
  Value = 0.0 [m]
  Variable = Y
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /ISOSURFACE:Isosurface Y 0, view=/VIEW:View 1""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >hide /ISOSURFACE:Isosurface Y 0, view=/VIEW:View 1""")
  results1.SendCommand(Command="> autolegend plot=/ISOSURFACE:Isosurface Pos Y 40, view=VIEW:View 1")
  results1.SendCommand(Command="""ISOSURFACE:Isosurface Pos Y 40
  Apply Instancing Transform = On
  Apply Texture = Off
  Blend Texture = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Colour = 0, 0, 0
  Line Colour Mode = Default
  Line Width = 1
  Max = 0.0 [m s^-1]
  Min = 0.0 [m s^-1]
  Range = Global
  Render Edge Angle = 0 [degree]
  Specular Lighting = On
  Surface Drawing = Smooth Shading
  Texture Angle = 0
  Texture Direction = 0 , 1 , 0 
  Texture File =  
  Texture Material = Metal
  Texture Position = 0 , 0 
  Texture Scale = 1
  Texture Type = Predefined
  Tile Texture = Off
  Transform Texture = Off
  Transparency = 0.0
  Value = 0.4 [m]
  Variable = Y
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /ISOSURFACE:Isosurface Pos Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >hide /ISOSURFACE:Isosurface Pos Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="> autolegend plot=/ISOSURFACE:Isosurface Neg Y 40, view=VIEW:View 1")
  results1.SendCommand(Command="""ISOSURFACE:Isosurface Neg Y 40
  Apply Instancing Transform = On
  Apply Texture = Off
  Blend Texture = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Colour = 0, 0, 0
  Line Colour Mode = Default
  Line Width = 1
  Max = 0.0 [m s^-1]
  Min = 0.0 [m s^-1]
  Range = Global
  Render Edge Angle = 0 [degree]
  Specular Lighting = On
  Surface Drawing = Smooth Shading
  Texture Angle = 0
  Texture Direction = 0 , 1 , 0 
  Texture File =  
  Texture Material = Metal
  Texture Position = 0 , 0 
  Texture Scale = 1
  Texture Type = Predefined
  Tile Texture = Off
  Transform Texture = Off
  Transparency = 0.0
  Value = -0.4 [m]
  Variable = Y
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /ISOSURFACE:Isosurface Neg Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >hide /ISOSURFACE:Isosurface Neg Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Streamline Y 0, view=VIEW:View 1")
  results1.SendCommand(Command="""STREAMLINE:Streamline Y 0
  Absolute Tolerance = 0.0 [m]
  Apply Instancing Transform = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Cross Periodics = On
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Draw Streams = On
  Draw Symbols = Off
  Grid Tolerance = 0.01
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Width = 1
  Location List = /ISOSURFACE:Isosurface Y 0
  Locator Sampling Method = Vertex
  Max = 0.0 [m s^-1]
  Maximum Number of Items = 150
  Min = 0.0 [m s^-1]
  Number of Samples = 500
  Number of Sides = 8
  Range = Global
  Reduction Factor = 1.0
  Reduction or Max Number = Max Number
  Sample Spacing = 0.1
  Sampling Aspect Ratio = 1
  Sampling Grid Angle = 0 [degree]
  Seed Point Type = Equally Spaced Samples
  Simplify Geometry = Off
  Specular Lighting = On
  Stream Drawing Mode = Line
  Stream Initial Direction = 0 , 0 , 0 
  Stream Size = 1.0
  Stream Symbol = Ball
  Streamline Direction = Forward and Backward
  Streamline Maximum Periods = 20
  Streamline Maximum Segments = 10000
  Streamline Maximum Time = 0.0 [s]
  Streamline Type = 3D Streamline
  Streamline Width = 2
  Surface Drawing = Smooth Shading
  Surface Streamline Direction = Forward and Backward
  Symbol Size = 1.0
  Symbol Start Time = 10.0 [s]
  Symbol Stop Time = -10.0 [s]
  Symbol Time Interval = 1.0 [s]
  Tolerance Mode = Grid Relative
  Transparency = 0.0
  Variable = Velocity
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /STREAMLINE:Streamline Y 0, view=/VIEW:View 1""")
  results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Streamline Pos Y 40, view=VIEW:View 1")
  results1.SendCommand(Command="""STREAMLINE:Streamline Pos Y 40
  Absolute Tolerance = 0.0 [m]
  Apply Instancing Transform = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Cross Periodics = On
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Draw Streams = On
  Draw Symbols = Off
  Grid Tolerance = 0.01
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Width = 1
  Location List = /ISOSURFACE:Isosurface Pos Y 40
  Locator Sampling Method = Vertex
  Max = 0.0 [m s^-1]
  Maximum Number of Items = 150
  Min = 0.0 [m s^-1]
  Number of Samples = 500
  Number of Sides = 8
  Range = Global
  Reduction Factor = 1.0
  Reduction or Max Number = Max Number
  Sample Spacing = 0.1
  Sampling Aspect Ratio = 1
  Sampling Grid Angle = 0 [degree]
  Seed Point Type = Equally Spaced Samples
  Simplify Geometry = Off
  Specular Lighting = On
  Stream Drawing Mode = Line
  Stream Initial Direction = 0 , 0 , 0 
  Stream Size = 1.0
  Stream Symbol = Ball
  Streamline Direction = Forward and Backward
  Streamline Maximum Periods = 20
  Streamline Maximum Segments = 10000
  Streamline Maximum Time = 0.0 [s]
  Streamline Type = 3D Streamline
  Streamline Width = 2
  Surface Drawing = Smooth Shading
  Surface Streamline Direction = Forward and Backward
  Symbol Size = 1.0
  Symbol Start Time = 10.0 [s]
  Symbol Stop Time = -10.0 [s]
  Symbol Time Interval = 1.0 [s]
  Tolerance Mode = Grid Relative
  Transparency = 0.0
  Variable = Velocity
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /STREAMLINE:Streamline Pos Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Streamline Neg Y 40, view=VIEW:View 1")
  results1.SendCommand(Command="""STREAMLINE:Streamline Neg Y 40
  Absolute Tolerance = 0.0 [m]
  Apply Instancing Transform = On
  Colour = 0.75, 0.75, 0.75
  Colour Map = Default Colour Map
  Colour Mode = Variable
  Colour Scale = Linear
  Colour Variable = Velocity
  Colour Variable Boundary Values = Conservative
  Cross Periodics = On
  Culling Mode = No Culling
  Domain List = /DOMAIN GROUP:All Domains
  Draw Faces = On
  Draw Lines = Off
  Draw Streams = On
  Draw Symbols = Off
  Grid Tolerance = 0.01
  Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
  Lighting = On
  Line Width = 1
  Location List = /ISOSURFACE:Isosurface Neg Y 40
  Locator Sampling Method = Vertex
  Max = 0.0 [m s^-1]
  Maximum Number of Items = 150
  Min = 0.0 [m s^-1]
  Number of Samples = 500
  Number of Sides = 8
  Range = Global
  Reduction Factor = 1.0
  Reduction or Max Number = Max Number
  Sample Spacing = 0.1
  Sampling Aspect Ratio = 1
  Sampling Grid Angle = 0 [degree]
  Seed Point Type = Equally Spaced Samples
  Simplify Geometry = Off
  Specular Lighting = On
  Stream Drawing Mode = Line
  Stream Initial Direction = 0 , 0 , 0 
  Stream Size = 1.0
  Stream Symbol = Ball
  Streamline Direction = Forward and Backward
  Streamline Maximum Periods = 20
  Streamline Maximum Segments = 10000
  Streamline Maximum Time = 0.0 [s]
  Streamline Type = 3D Streamline
  Streamline Width = 2
  Surface Drawing = Smooth Shading
  Surface Streamline Direction = Forward and Backward
  Symbol Size = 1.0
  Symbol Start Time = 10.0 [s]
  Symbol Stop Time = -10.0 [s]
  Symbol Time Interval = 1.0 [s]
  Tolerance Mode = Grid Relative
  Transparency = 0.0
  Variable = Velocity
  Variable Boundary Values = Conservative
    OBJECT VIEW TRANSFORM:
    Apply Reflection = Off
    Apply Rotation = Off
    Apply Scale = Off
    Apply Translation = Off
    Principal Axis = Z
    Reflection Plane Option = XY Plane
    Rotation Angle = 0.0 [degree]
    Rotation Axis From = 0 [m], 0 [m], 0 [m]
    Rotation Axis To = 0 [m], 0 [m], 0 [m]
    Rotation Axis Type = Principal Axis
    Scale Vector = 1 , 1 , 1 
    Translation Vector = 0 [m], 0 [m], 0 [m]
    X = 0.0 [m]
    Y = 0.0 [m]
    Z = 0.0 [m]
    END
  END""")
  results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
  >show /STREAMLINE:Streamline Neg Y 40, view=/VIEW:View 1""")
  results1.SendCommand(Command="""VIEW:View 1
  Camera Mode = User Specified
  CAMERA:
  Option = Pivot Point and Quaternion
  Pivot Point = 2.51148, 0.64251, 0.68061
  Scale = 0.803174
  Pan = 2.19897, -0.011249
  Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17

  END

  END

  > update
  ANIMATION:ANIMATION
  QAnim MPEG Filename = {}/Trailing Edge and Wake Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4

  END""".format(filepaths[num]))
  results1.SendCommand(Command="""ANIMATION:
  Animation Bit Rate = 5152000
  Animation Frame Rate = 24
  Animation Quality = Highest
  Animation Speed Factor = 2
  Antialiasing = On
  Drop Last MPEG Frame = Off
  Hardcopy Tolerance = 0.0001
  Intermediate File Format = jpg
  Keep Intermediate Files = Off
  MPEG Height = 1080
  MPEG Scale = 100
  MPEG Size = 1080p
  MPEG Width = 1920
  Output Directory = .
  Output to User Directory = Off
  QAnim Override Symbol = On
  QAnim Symbol Size = 0.05
  QAnim Symbol Spacing = 0.3
  QAnim Symbol Type = Ball
  Screen Capture = Off
  Speed Adjustment Selection = Normal
  Speed Scaling Method = Distribute Frames Smoothly
  Timestep Interpolation Method = Timestep
  Variable Bit Rate = On
  White Background = Off
  END""")
  results1.SendCommand(Command="""ANIMATION: ANIMATION
  QAnim Object List = /STREAMLINE:Streamline Neg Y 40,/STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
  QAnim Frames = 100
  QAnim MPEG Filename = {}/Trailing Edge and Wake Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4
  END
  >animate quickAnimate""".format(filepaths[num]))
  results1.SendCommand(Command="""VIEW:View 1
    Camera Mode = User Specified
    CAMERA:
      Option = Pivot Point and Quaternion
      Pivot Point = 4.4939, 0.459533, 0.511379
      Scale = 0.624333
      Pan = 0.756583, -0.215757
      Rotation Quaternion = -3.72529e-09, 0.707107, 0.707107, -3.72529e-09
      
    END

  END

  > update
  QAnim MPEG Filename = {}/Trailing Edge and Wake 2 Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4

  END""".format(filepaths[num]))
  results1.SendCommand(Command="""ANIMATION: ANIMATION
  QAnim Object List = /STREAMLINE:Streamline Neg Y 40,/STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
  QAnim Frames = 100
  QAnim MPEG Filename = {}/Trailing Edge and Wake 2 Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4
  END
  >animate quickAnimate""".format(filepaths[num]))
  results1.SendCommand(Command="""VIEW:View 1
    Camera Mode = User Specified
    CAMERA:
      Option = Pivot Point and Quaternion
      Pivot Point = 4.4939, 0.459533, 0.511379
      Scale = 0.860138
      Pan = -1.27971, -0.419625
      Rotation Quaternion = -3.72529e-09, 0.707107, 0.707107, -3.72529e-09
      
    END

  END

  > update
  ANIMATION:ANIMATION
  QAnim MPEG Filename = {}/Canopy Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4

  END""".format(filepaths[num]))
  results1.SendCommand(Command="""ANIMATION: ANIMATION
  QAnim Object List = /STREAMLINE:Streamline Neg Y 40,/STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
  QAnim Frames = 100
  QAnim MPEG Filename = {}/Canopy Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4
  END
  >animate quickAnimate""".format(filepaths[num]))
  results1.SendCommand(Command="""VIEW:View 1
    Camera Mode = User Specified
    CAMERA:
      Option = Pivot Point and Quaternion
      Pivot Point = 3.23676, 0.504839, 0.995587
      Scale = 0.289498
      Pan = -0.24374, -1.06636
      Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17
      
    END

  END

  > update
  ANIMATION:ANIMATION
  QAnim MPEG Filename = {}/Right Side Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4

  END""".format(filepaths[num]))
  results1.SendCommand(Command="""ANIMATION: ANIMATION
  QAnim Object List = /STREAMLINE:Streamline Neg Y 40,/STREAMLINE:Streamline Pos Y 40,/STREAMLINE:Streamline Y 0
  QAnim Frames = 100
  QAnim MPEG Filename = {}/Right Side Streamline Animation.mp4
  QAnim Save MPEG = On
  QAnim Looping = Loop
  QAnim Looping Cycles = 1
  Video Format = mp4
  END
  >animate quickAnimate""".format(filepaths[num]))
  results1.Exit()