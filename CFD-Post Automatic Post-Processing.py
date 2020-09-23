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
if queue >= 1:
    template1 = GetTemplate(TemplateName="Results")
    system1 = GetSystem(Name="FLU")
    system2 = template1.CreateSystem(
        Position="Right",
        RelativeTo=system1)
    solutionComponent1 = system1.GetComponent(Name="Solution")
    resultsComponent1 = system2.GetComponent(Name="Results")
    solutionComponent1.TransferData(TargetComponent=resultsComponent1)
    results1 = system2.GetContainer(ComponentName="Results")
    results1.Edit()
    results1.SendCommand(Command="""VIEW:View 1
      Light Angle = 50, 110
    END

    VIEW:View 2
      Light Angle = 50, 110
    END

    VIEW:View 3
      Light Angle = 50, 110
    END

    VIEW:View 4
      Light Angle = 50, 110
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /DATA READER/CASE:Case {}/BOUNDARY:car, view=/VIEW:View 1""".format(modules[0]))
    results1.SendCommand(Command="> autolegend plot=/CONTOUR:TKE Contour, view=VIEW:View 1")
    results1.SendCommand(Command="""CONTOUR:TKE Contour
    Apply Instancing Transform = On
    Clip Contour = Off
    Colour Map = Default Colour Map
    Colour Scale = Logarithmic
    Colour Variable = Turbulence Kinetic Energy
    Colour Variable Boundary Values = Conservative
    Constant Contour Colour = Off
    Contour Range = Global
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Contours = Off
    Font = Sans Serif
    Fringe Fill = On
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Location List = car
    Max = 0.0 [m^2 s^-2]
    Min = 0.0 [m^2 s^-2]
    Number of Contours = 5000
    Show Numbers = Off
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Text Colour = 0, 0, 0
    Text Colour Mode = Default
    Text Height = 0.024
    Transparency = 0.0
    Use Face Values = On
    Value List = 0 [m^2 s^-2],1 [m^2 s^-2]
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/CONTOUR:Pressure Contour, view=VIEW:View 1")
    results1.SendCommand(Command="""CONTOUR:Pressure Contour
    Apply Instancing Transform = On
    Clip Contour = Off
    Colour Map = Default Colour Map
    Colour Scale = Linear
    Colour Variable = Pressure
    Colour Variable Boundary Values = Conservative
    Constant Contour Colour = Off
    Contour Range = Global
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Contours = Off
    Font = Sans Serif
    Fringe Fill = On
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Location List = car
    Max = 0.0 [Pa]
    Min = 0.0 [Pa]
    Number of Contours = 5000
    Show Numbers = Off
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Text Colour = 0, 0, 0
    Text Colour Mode = Default
    Text Height = 0.024
    Transparency = 0.0
    Use Face Values = On
    Value List = 0 [Pa],1 [Pa]
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Wall Shear Streamline, view=VIEW:View 1")
    results1.SendCommand(Command="""STREAMLINE:Wall Shear Streamline
    Absolute Tolerance = 0.0 [m]
    Apply Instancing Transform = On
    Colour = 0, 0, 1
    Colour Map = Default Colour Map
    Colour Mode = Constant
    Colour Scale = Linear
    Colour Variable = Wall Shear
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
    Location List = car
    Locator Sampling Method = Equally Spaced
    Max = 0.0 [Pa]
    Maximum Number of Items = 25
    Min = 0.0 [Pa]
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
    Streamline Direction = Forward
    Streamline Maximum Periods = 20
    Streamline Maximum Segments = 10000
    Streamline Maximum Time = 0.0 [s]
    Streamline Type = Surface Streamline
    Streamline Width = 2
    Surface Drawing = Smooth Shading
    Surface Streamline Direction = Forward and Backward
    Symbol Size = 1.0
    Symbol Start Time = 10.0 [s]
    Symbol Stop Time = -10.0 [s]
    Symbol Time Interval = 1.0 [s]
    Tolerance Mode = Grid Relative
    Transparency = 0.0
    Variable = Wall Shear
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
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""LIBRARY:
      CEL:
        EXPRESSIONS:
          Cp Expr = (Pressure - Reference Pressure ) / (0.5 * areaAve(Density)@inlet * areaAve(Velocity)@inlet^2)
        END
      END
    END

    EXPRESSION EVALUATOR:
      Evaluated Expression = Cp Expr
    END

    > forceupdate EXPRESSION EVALUATOR""")
    results1.SendCommand(Command="""USER SCALAR VARIABLE:Cp Var
    Boundary Values = Conservative
    Calculate Global Range = On
    Expression = Cp Expr
    Recipe = Expression
    Variable to Copy = Pressure
    Variable to Gradient = Pressure
    END""")
    results1.SendCommand(Command="> autolegend plot=/CONTOUR:Cp Contour, view=VIEW:View 1")
    results1.SendCommand(Command="""CONTOUR:Cp Contour
    Apply Instancing Transform = On
    Clip Contour = Off
    Colour Map = Default Colour Map
    Colour Scale = Linear
    Colour Variable = Cp Var
    Colour Variable Boundary Values = Conservative
    Constant Contour Colour = Off
    Contour Range = Local
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Contours = Off
    Font = Sans Serif
    Fringe Fill = On
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Location List = car
    Max = 0.0
    Min = 0.0
    Number of Contours = 5000
    Show Numbers = Off
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Text Colour = 0, 0, 0
    Text Colour Mode = Default
    Text Height = 0.024
    Transparency = 0.0
    Use Face Values = On
    Value List = 0,1
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
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/ISOSURFACE:Y 0 Plane, view=VIEW:View 1")
    results1.SendCommand(Command="""ISOSURFACE:Y 0 Plane
    Apply Instancing Transform = On
    Apply Texture = Off
    Blend Texture = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Use Plot Variable
    Colour Scale = Linear
    Colour Variable = Y
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
    Max = 0.0 [m]
    Min = 0.0 [m]
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
    >show /ISOSURFACE:Y 0 Plane, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /ISOSURFACE:Y 0 Plane, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/POLYLINE:Centerline Polyline, view=VIEW:View 1")
    results1.SendCommand(Command="""POLYLINE:Centerline Polyline
    Apply Instancing Transform = On
    Boundary List = car
    Colour = 0, 1, 0
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Cp Var
    Colour Variable Boundary Values = Conservative
    Contour Level = 1
    Domain List = /DOMAIN GROUP:All Domains
    Input File =  
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Line Width = 15
    Location = /ISOSURFACE:Y 0 Plane
    Max = 0.0
    Min = 0.0
    Option = Boundary Intersection
    Range = Global
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
    >show /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""CHART:Cp vs X Coord
    Chart Axes Font = Tahoma, 10, False, False, False, False
    Chart Axes Titles Font = Tahoma, 10, True, False, False, False
    Chart Grid Line Width = 1
    Chart Horizontal Grid = On
    Chart Legend = On
    Chart Legend Font = Tahoma, 8, False, False, False, False
    Chart Legend Inside = Outside Chart
    Chart Legend Justification = Center
    Chart Legend Position = Bottom
    Chart Legend Width Height = 0.2 , 0.4 
    Chart Legend X Justification = Right
    Chart Legend XY Position = 0.73 , 0.275 
    Chart Legend Y Justification = Center
    Chart Line Width = 2
    Chart Lines Order = Series 1,Chart Line 1
    Chart Minor Grid = Off
    Chart Minor Grid Line Width = 1
    Chart Symbol Size = 4
    Chart Title = Cp vs X Coordinate
    Chart Title Font = Tahoma, 12, True, False, False, False
    Chart Title Visibility = On
    Chart Type = XY
    Chart Vertical Grid = On
    Chart X Axis Automatic Number Formatting = On
    Chart X Axis Label = X Axis <units>
    Chart X Axis Number Format = %10.3e
    Chart Y Axis Automatic Number Formatting = On
    Chart Y Axis Label = Y Axis <units>
    Chart Y Axis Number Format = %10.3e
    Default Chart X Variable = X
    Default Chart Y Variable = Cp Var
    Default Difference Line Calculation = From Points
    Default Histogram Y Axis Weighting = None
    Default Time Chart Variable = Pressure
    Default Time Chart X Expression = Time
    Default Time Variable Absolute Value = Off
    Default Time Variable Boundary Values = Conservative
    Default X Variable Absolute Value = Off
    Default X Variable Boundary Values = Conservative
    Default Y Variable Absolute Value = Off
    Default Y Variable Boundary Values = Conservative
    FFT Full Input Range = On
    FFT Max = 0.0
    FFT Min = 0.0
    FFT Subtract Mean = Off
    FFT Window Type = Hanning
    FFT X Function = Frequency
    FFT Y Function = Power Spectral Density
    Histogram Automatic Divisions = Automatic
    Histogram Divisions = -1.0,1.0
    Histogram Divisions Count = 10
    Histogram Y Axis Value = Count
    Is FFT Chart = Off
    Max X = 1.0
    Max Y = 1.0
    Min X = -1.0
    Min Y = -1.0
    Use Data For X Axis Labels = On
    Use Data For Y Axis Labels = On
    X Axis Automatic Range = On
    X Axis Inverted = Off
    X Axis Logarithmic Scaling = Off
    Y Axis Automatic Range = On
    Y Axis Inverted = Off
    Y Axis Logarithmic Scaling = Off
      CHART SERIES:Series 1
      Chart Line Custom Data Selection = Off
      Chart Line Filename =  
      Chart Series Type = Regular
      Location = /POLYLINE:Centerline Polyline
      Monitor Data Filename =  
      Monitor Data Source = Case
      Monitor Data X Variable Absolute Value = Off
      Monitor Data Y Variable Absolute Value = Off
      Operating Point Data Case = Case {}
      Operating Point Data Filename =  
      Operating Point Data Source = File
      Series Name = Series 1
      Time Chart Expression = Time
      Time Chart Type = Point
        CHART LINE:Chart Line 1
        Auto Chart Line Colour = On
        Auto Chart Symbol Colour = On
        Chart FFT Line Type = Bars
        Chart Line Colour = 1.0, 0.0, 0.0
        Chart Line Style = Automatic
        Chart Line Type = Lines
        Chart Line Visibility = On
        Chart Symbol Colour = 0.0, 1.0, 0.0
        Chart Symbol Style = Automatic
        Fill Area = On
        Fill Area Options = Automatic
        Is Valid = True
        Line Name = Series 1
        Use Automatic Line Naming = On
        END
      END
      OBJECT REPORT OPTIONS:
          Report Caption = Pressure coefficient along centerline of car by distance along X axis from nose of car
      END
    END""".format(modules[0]))
    results1.SendCommand(Command=">chart print, Chart Name = /CHART:Cp vs X Coord, filename = {}/Cp vs X Coord.png, x size = 2000, y size = 2000, format = png, factor = 1.83074".format(filepaths[0]))
    results1.SendCommand(Command="> report hideItem=/CHART:Cp vs X Coord")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /WIREFRAME:Wireframe, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.655433
        Pan = -0.0111499, -0.372659
        Rotation Quaternion = -0.707107, 0, 0, 0.707107
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.512924
        Pan = 0, 0
        Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.689005
        Pan = -0.0972085, -0.337592
        Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename ={}/TKE Contour 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 1.59745
        Pan = 0, 0
        Rotation Quaternion = -0.5, 0.5, 0.5, 0.5
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 1.59745
        Pan = 0, 0
        Rotation Quaternion = -0.5, -0.5, -0.5, 0.5
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.609706
        Pan = 0, 0
        Rotation Quaternion = 0, 0, 0, 1
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.624948
        Pan = -0.141048, -0.546109
        Rotation Quaternion = 0, 0, 0, 1
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.640572
        Pan = -0.079174, -0.550776
        Rotation Quaternion = 1, 4.47035e-08, -6.12324e-17, 1.44757e-24
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.640572
        Pan = -0.079174, -0.550776
        Rotation Quaternion = 0.611682, -0.00437015, -0.0498028, -0.789522
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.707071
        Pan = 0.0309811, -0.313254
        Rotation Quaternion = 0.16889, 0.490153, 0.833347, -0.191657
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.656586
        Pan = 0.154765, -0.404108
        Rotation Quaternion = -0.466997, 0.0118956, -0.123012, 0.87557
        
      END

    END

    VIEW:View 1
      Light Angle = 90.0881, 104.046
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = 0.00328224, -0.331506
        Rotation Quaternion = -0.863355, 0.0798891, -0.128229, 0.481439
        
      END

    END

    VIEW:View 1
      Light Angle = 126.207, 83.4066
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = -0.0328224, -0.246168
        Rotation Quaternion = -0.866455, 0.0319442, -0.101365, 0.487802
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Wall Shear Streamline, view=VIEW:View 1")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = -0.0328224, -0.246168
        Rotation Quaternion = -0.0665846, -0.813088, -0.53828, 0.211405
        
      END

    END

    VIEW:View 1
      Light Angle = 95.0494, 82.0174
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = -0.0328224, -0.246168
        Rotation Quaternion = -0.0149095, -0.854263, -0.494958, 0.15814
        
      END

    END

    VIEW:View 1
      Light Angle = 89.0957, 75.2699
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command="> report showItem=/CHART:Cp vs X Coord")
    results1.SendCommand(Command="""EXPORT:
     Export File = {}/Cp vs X Coord.csv
     Export Chart Name = Cp vs X Coord
     Overwrite = On
    END
    >export chart""".format(filepaths[0]))
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.512924
        Pan = 0, 0
        Rotation Quaternion = -0.707107, 0, 0, 0.707107
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /DATA READER/CASE:Case {}/BOUNDARY:car, view=/VIEW:View 1""".format(modules[0]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.656586
        Pan = 0.0997342, -0.360136
        Rotation Quaternion = -0.707107, 0, 0, 0.707107
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Centerline Polyline.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command=">setPreferences Viewer Background Colour Type = Solid, Viewer Background Image File =  , Viewer Background Colour = 0&0&0, Global Text Colour = 1&1&1")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Centerline Polyline Black.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[0]))
    results1.SendCommand(Command=">setPreferences Viewer Background Type = Colour, Viewer Background Colour Type = Top-Bottom Gradient, Viewer Background Colour = 0.42&0.55&0.871, Viewer Background Colour 2 = 1&1&1, Global Text Colour = 0&0&0, Global Edge Colour = 0&0&0")
    results1.Exit()
    

for num in range(1,queue):
    template1 = GetTemplate(TemplateName="Results")
    system1 = GetSystem(Name="FLU {}".format(num))
    system2 = template1.CreateSystem(
        Position="Right",
        RelativeTo=system1)
    solutionComponent1 = system1.GetComponent(Name="Solution")
    resultsComponent1 = system2.GetComponent(Name="Results")
    solutionComponent1.TransferData(TargetComponent=resultsComponent1)
    results1 = system2.GetContainer(ComponentName="Results")
    results1.Edit()
    results1.SendCommand(Command="""VIEW:View 1
      Light Angle = 50, 110
    END

    VIEW:View 2
      Light Angle = 50, 110
    END

    VIEW:View 3
      Light Angle = 50, 110
    END

    VIEW:View 4
      Light Angle = 50, 110
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /DATA READER/CASE:Case {}/BOUNDARY:car, view=/VIEW:View 1""".format(modules[num]))
    results1.SendCommand(Command="> autolegend plot=/CONTOUR:TKE Contour, view=VIEW:View 1")
    results1.SendCommand(Command="""CONTOUR:TKE Contour
    Apply Instancing Transform = On
    Clip Contour = Off
    Colour Map = Default Colour Map
    Colour Scale = Logarithmic
    Colour Variable = Turbulence Kinetic Energy
    Colour Variable Boundary Values = Conservative
    Constant Contour Colour = Off
    Contour Range = Global
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Contours = Off
    Font = Sans Serif
    Fringe Fill = On
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Location List = car
    Max = 0.0 [m^2 s^-2]
    Min = 0.0 [m^2 s^-2]
    Number of Contours = 5000
    Show Numbers = Off
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Text Colour = 0, 0, 0
    Text Colour Mode = Default
    Text Height = 0.024
    Transparency = 0.0
    Use Face Values = On
    Value List = 0 [m^2 s^-2],1 [m^2 s^-2]
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/CONTOUR:Pressure Contour, view=VIEW:View 1")
    results1.SendCommand(Command="""CONTOUR:Pressure Contour
    Apply Instancing Transform = On
    Clip Contour = Off
    Colour Map = Default Colour Map
    Colour Scale = Linear
    Colour Variable = Pressure
    Colour Variable Boundary Values = Conservative
    Constant Contour Colour = Off
    Contour Range = Global
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Contours = Off
    Font = Sans Serif
    Fringe Fill = On
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Location List = car
    Max = 0.0 [Pa]
    Min = 0.0 [Pa]
    Number of Contours = 5000
    Show Numbers = Off
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Text Colour = 0, 0, 0
    Text Colour Mode = Default
    Text Height = 0.024
    Transparency = 0.0
    Use Face Values = On
    Value List = 0 [Pa],1 [Pa]
      OBJECT VIEW TRANSFORM:
      Apply Reflection = Off
      Apply Rotation = Off
      Apply Scale = Off
      Apply Translation = Off
      END
    END""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Wall Shear Streamline, view=VIEW:View 1")
    results1.SendCommand(Command="""STREAMLINE:Wall Shear Streamline
    Absolute Tolerance = 0.0 [m]
    Apply Instancing Transform = On
    Colour = 0, 0, 1
    Colour Map = Default Colour Map
    Colour Mode = Constant
    Colour Scale = Linear
    Colour Variable = Wall Shear
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
    Location List = car
    Locator Sampling Method = Equally Spaced
    Max = 0.0 [Pa]
    Maximum Number of Items = 25
    Min = 0.0 [Pa]
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
    Streamline Direction = Forward
    Streamline Maximum Periods = 20
    Streamline Maximum Segments = 10000
    Streamline Maximum Time = 0.0 [s]
    Streamline Type = Surface Streamline
    Streamline Width = 2
    Surface Drawing = Smooth Shading
    Surface Streamline Direction = Forward and Backward
    Symbol Size = 1.0
    Symbol Start Time = 10.0 [s]
    Symbol Stop Time = -10.0 [s]
    Symbol Time Interval = 1.0 [s]
    Tolerance Mode = Grid Relative
    Transparency = 0.0
    Variable = Wall Shear
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
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""LIBRARY:
      CEL:
        EXPRESSIONS:
          Cp Expr = (Pressure - Reference Pressure ) / (0.5 * areaAve(Density)@inlet * areaAve(Velocity)@inlet^2)
        END
      END
    END

    EXPRESSION EVALUATOR:
      Evaluated Expression = Cp Expr
    END

    > forceupdate EXPRESSION EVALUATOR""")
    results1.SendCommand(Command="""USER SCALAR VARIABLE:Cp Var
    Boundary Values = Conservative
    Calculate Global Range = On
    Expression = Cp Expr
    Recipe = Expression
    Variable to Copy = Pressure
    Variable to Gradient = Pressure
    END""")
    results1.SendCommand(Command="> autolegend plot=/CONTOUR:Cp Contour, view=VIEW:View 1")
    results1.SendCommand(Command="""CONTOUR:Cp Contour
    Apply Instancing Transform = On
    Clip Contour = Off
    Colour Map = Default Colour Map
    Colour Scale = Linear
    Colour Variable = Cp Var
    Colour Variable Boundary Values = Conservative
    Constant Contour Colour = Off
    Contour Range = Local
    Culling Mode = No Culling
    Domain List = /DOMAIN GROUP:All Domains
    Draw Contours = Off
    Font = Sans Serif
    Fringe Fill = On
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Lighting = On
    Line Colour = 0, 0, 0
    Line Colour Mode = Default
    Line Width = 1
    Location List = car
    Max = 0.0
    Min = 0.0
    Number of Contours = 5000
    Show Numbers = Off
    Specular Lighting = On
    Surface Drawing = Smooth Shading
    Text Colour = 0, 0, 0
    Text Colour Mode = Default
    Text Height = 0.024
    Transparency = 0.0
    Use Face Values = On
    Value List = 0,1
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
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/ISOSURFACE:Y 0 Plane, view=VIEW:View 1")
    results1.SendCommand(Command="""ISOSURFACE:Y 0 Plane
    Apply Instancing Transform = On
    Apply Texture = Off
    Blend Texture = On
    Colour = 0.75, 0.75, 0.75
    Colour Map = Default Colour Map
    Colour Mode = Use Plot Variable
    Colour Scale = Linear
    Colour Variable = Y
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
    Max = 0.0 [m]
    Min = 0.0 [m]
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
    >show /ISOSURFACE:Y 0 Plane, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /ISOSURFACE:Y 0 Plane, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/POLYLINE:Centerline Polyline, view=VIEW:View 1")
    results1.SendCommand(Command="""POLYLINE:Centerline Polyline
    Apply Instancing Transform = On
    Boundary List = car
    Colour = 0, 1, 0
    Colour Map = Default Colour Map
    Colour Mode = Variable
    Colour Scale = Linear
    Colour Variable = Cp Var
    Colour Variable Boundary Values = Conservative
    Contour Level = 1
    Domain List = /DOMAIN GROUP:All Domains
    Input File =  
    Instancing Transform = /DEFAULT INSTANCE TRANSFORM:Default Transform
    Line Width = 15
    Location = /ISOSURFACE:Y 0 Plane
    Max = 0.0
    Min = 0.0
    Option = Boundary Intersection
    Range = Global
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
    >show /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""CHART:Cp vs X Coord
    Chart Axes Font = Tahoma, 10, False, False, False, False
    Chart Axes Titles Font = Tahoma, 10, True, False, False, False
    Chart Grid Line Width = 1
    Chart Horizontal Grid = On
    Chart Legend = On
    Chart Legend Font = Tahoma, 8, False, False, False, False
    Chart Legend Inside = Outside Chart
    Chart Legend Justification = Center
    Chart Legend Position = Bottom
    Chart Legend Width Height = 0.2 , 0.4 
    Chart Legend X Justification = Right
    Chart Legend XY Position = 0.73 , 0.275 
    Chart Legend Y Justification = Center
    Chart Line Width = 2
    Chart Lines Order = Series 1,Chart Line 1
    Chart Minor Grid = Off
    Chart Minor Grid Line Width = 1
    Chart Symbol Size = 4
    Chart Title = Cp vs X Coordinate
    Chart Title Font = Tahoma, 12, True, False, False, False
    Chart Title Visibility = On
    Chart Type = XY
    Chart Vertical Grid = On
    Chart X Axis Automatic Number Formatting = On
    Chart X Axis Label = X Axis <units>
    Chart X Axis Number Format = %10.3e
    Chart Y Axis Automatic Number Formatting = On
    Chart Y Axis Label = Y Axis <units>
    Chart Y Axis Number Format = %10.3e
    Default Chart X Variable = X
    Default Chart Y Variable = Cp Var
    Default Difference Line Calculation = From Points
    Default Histogram Y Axis Weighting = None
    Default Time Chart Variable = Pressure
    Default Time Chart X Expression = Time
    Default Time Variable Absolute Value = Off
    Default Time Variable Boundary Values = Conservative
    Default X Variable Absolute Value = Off
    Default X Variable Boundary Values = Conservative
    Default Y Variable Absolute Value = Off
    Default Y Variable Boundary Values = Conservative
    FFT Full Input Range = On
    FFT Max = 0.0
    FFT Min = 0.0
    FFT Subtract Mean = Off
    FFT Window Type = Hanning
    FFT X Function = Frequency
    FFT Y Function = Power Spectral Density
    Histogram Automatic Divisions = Automatic
    Histogram Divisions = -1.0,1.0
    Histogram Divisions Count = 10
    Histogram Y Axis Value = Count
    Is FFT Chart = Off
    Max X = 1.0
    Max Y = 1.0
    Min X = -1.0
    Min Y = -1.0
    Use Data For X Axis Labels = On
    Use Data For Y Axis Labels = On
    X Axis Automatic Range = On
    X Axis Inverted = Off
    X Axis Logarithmic Scaling = Off
    Y Axis Automatic Range = On
    Y Axis Inverted = Off
    Y Axis Logarithmic Scaling = Off
      CHART SERIES:Series 1
      Chart Line Custom Data Selection = Off
      Chart Line Filename =  
      Chart Series Type = Regular
      Location = /POLYLINE:Centerline Polyline
      Monitor Data Filename =  
      Monitor Data Source = Case
      Monitor Data X Variable Absolute Value = Off
      Monitor Data Y Variable Absolute Value = Off
      Operating Point Data Case = Case {}
      Operating Point Data Filename =  
      Operating Point Data Source = File
      Series Name = Series 1
      Time Chart Expression = Time
      Time Chart Type = Point
        CHART LINE:Chart Line 1
        Auto Chart Line Colour = On
        Auto Chart Symbol Colour = On
        Chart FFT Line Type = Bars
        Chart Line Colour = 1.0, 0.0, 0.0
        Chart Line Style = Automatic
        Chart Line Type = Lines
        Chart Line Visibility = On
        Chart Symbol Colour = 0.0, 1.0, 0.0
        Chart Symbol Style = Automatic
        Fill Area = On
        Fill Area Options = Automatic
        Is Valid = True
        Line Name = Series 1
        Use Automatic Line Naming = On
        END
      END
      OBJECT REPORT OPTIONS:
          Report Caption = Pressure coefficient along centerline of car by distance along X axis from nose of car
      END
    END""".format(modules[num]))
    results1.SendCommand(Command=">chart print, Chart Name = /CHART:Cp vs X Coord, filename = {}/Cp vs X Coord.png, x size = 2000, y size = 2000, format = png, factor = 1.83074".format(filepaths[num]))
    results1.SendCommand(Command="> report hideItem=/CHART:Cp vs X Coord")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /WIREFRAME:Wireframe, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.655433
        Pan = -0.0111499, -0.372659
        Rotation Quaternion = -0.707107, 0, 0, 0.707107
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 01 Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.512924
        Pan = 0, 0
        Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.689005
        Pan = -0.0972085, -0.337592
        Rotation Quaternion = -4.32978e-17, 0.707107, 0.707107, 4.32978e-17
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename ={}/TKE Contour 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 02 Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 1.59745
        Pan = 0, 0
        Rotation Quaternion = -0.5, 0.5, 0.5, 0.5
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 03 Front.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 1.59745
        Pan = 0, 0
        Rotation Quaternion = -0.5, -0.5, -0.5, 0.5
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 04 Rear.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.609706
        Pan = 0, 0
        Rotation Quaternion = 0, 0, 0, 1
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.624948
        Pan = -0.141048, -0.546109
        Rotation Quaternion = 0, 0, 0, 1
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 05 Top.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.640572
        Pan = -0.079174, -0.550776
        Rotation Quaternion = 1, 4.47035e-08, -6.12324e-17, 1.44757e-24
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 06 Bottom.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.640572
        Pan = -0.079174, -0.550776
        Rotation Quaternion = 0.611682, -0.00437015, -0.0498028, -0.789522
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.707071
        Pan = 0.0309811, -0.313254
        Rotation Quaternion = 0.16889, 0.490153, 0.833347, -0.191657
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 07 Top Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.656586
        Pan = 0.154765, -0.404108
        Rotation Quaternion = -0.466997, 0.0118956, -0.123012, 0.87557
        
      END

    END

    VIEW:View 1
      Light Angle = 90.0881, 104.046
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 08 Top Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = 0.00328224, -0.331506
        Rotation Quaternion = -0.863355, 0.0798891, -0.128229, 0.481439
        
      END

    END

    VIEW:View 1
      Light Angle = 126.207, 83.4066
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = -0.0328224, -0.246168
        Rotation Quaternion = -0.866455, 0.0319442, -0.101365, 0.487802
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="> autolegend plot=/STREAMLINE:Wall Shear Streamline, view=VIEW:View 1")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 09 Bottom Left.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = -0.0328224, -0.246168
        Rotation Quaternion = -0.0665846, -0.813088, -0.53828, 0.211405
        
      END

    END

    VIEW:View 1
      Light Angle = 95.0494, 82.0174
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.671819
        Pan = -0.0328224, -0.246168
        Rotation Quaternion = -0.0149095, -0.854263, -0.494958, 0.15814
        
      END

    END

    VIEW:View 1
      Light Angle = 89.0957, 75.2699
    END

    > update
    # Sending visibility action from ViewUtilities
    >show /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Contour 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Cp Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Pressure Contour 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:Pressure Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/TKE Contour 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /CONTOUR:TKE Contour, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Wall Shear Streamline 10 Bottom Right.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command="> report showItem=/CHART:Cp vs X Coord")
    results1.SendCommand(Command="""EXPORT:
     Export File = {}/Cp vs X Coord.csv
     Export Chart Name = Cp vs X Coord
     Overwrite = On
    END
    >export chart""".format(filepaths[num]))
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.512924
        Pan = 0, 0
        Rotation Quaternion = -0.707107, 0, 0, 0.707107
        
      END

    END

    > update
    # Sending visibility action from ViewUtilities
    >hide /STREAMLINE:Wall Shear Streamline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >hide /DATA READER/CASE:Case {}/BOUNDARY:car, view=/VIEW:View 1""".format(modules[num]))
    results1.SendCommand(Command="""# Sending visibility action from ViewUtilities
    >show /POLYLINE:Centerline Polyline, view=/VIEW:View 1""")
    results1.SendCommand(Command="""VIEW:View 1
      Camera Mode = User Specified
      CAMERA:
        Option = Pivot Point and Quaternion
        Pivot Point = 2.45395, 0, 0.584167
        Scale = 0.656586
        Pan = 0.0997342, -0.360136
        Rotation Quaternion = -0.707107, 0, 0, 0.707107
        
      END

    END

    > update
    HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Centerline Polyline.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command=">setPreferences Viewer Background Colour Type = Solid, Viewer Background Image File =  , Viewer Background Colour = 0&0&0, Global Text Colour = 1&1&1")
    results1.SendCommand(Command="""HARDCOPY:
    Antialiasing = On
    Hardcopy Filename = {}/Cp Centerline Polyline Black.png
    Hardcopy Format = png
    Hardcopy Tolerance = 0.0001
    Image Height = 4000
    Image Scale = 100
    Image Width = 8000
    JPEG Image Quality = 80
    Screen Capture = Off
    Use Screen Size = Off
    White Background = Off
    END
    >print""".format(filepaths[num]))
    results1.SendCommand(Command=">setPreferences Viewer Background Type = Colour, Viewer Background Colour Type = Top-Bottom Gradient, Viewer Background Colour = 0.42&0.55&0.871, Viewer Background Colour 2 = 1&1&1, Global Text Colour = 0&0&0, Global Edge Colour = 0&0&0")
    results1.Exit()