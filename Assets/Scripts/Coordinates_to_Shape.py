import bpy

# Beispiel: Liste von Weltkoordinaten im WGS84-Format
coordinates = [

]


# Funktion zur Umrechnung von WGS84 in Blender-Koordinaten
def wgs84_to_blender(coord):
    # Faktor für Längen- und Breitengrade in Blender (vereinfacht)
    scale_factor = 111319.9  # ungefähr 111.32 Kilometer pro Längengrad

    # Umrechnung der Längen- und Breitengrade in Meter
    x = (coord[0] - coordinates[0][0]) * 40075 * 1.8
    y = (coord[1] - coordinates[0][1]) * scale_factor * 0.9

    # Höhenangabe wird in den Ursprung verschoben
    z = coord[2] - coordinates[0][2]

    return (x, y, z)

# Funktion zum Erstellen der 3D-Form
def create_shape(coordinates):
    # Erstelle eine neue Mesh-Datenstruktur
    mesh = bpy.data.meshes.new(name="CustomShape")
    obj = bpy.data.objects.new("CustomObject", mesh)

    # Füge den neuen Mesh-Objekt zum aktuellen Szenenobjekt hinzu
    bpy.context.scene.collection.objects.link(obj)

    # Wähle das neue Objekt aus und mache es aktiv
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Füge die neuen Vertices basierend auf den Weltkoordinaten hinzu
    bpy.ops.object.mode_set(mode='OBJECT')
    mesh = bpy.context.object.data
    num_vertices = len(coordinates)

    if num_vertices < 2:
        return

    for i in range(num_vertices):
        mesh.vertices.add(1)
        mesh.vertices[-1].co = coordinates[i]

        if i > 0:
            # Verbinde den aktuellen Vertex mit dem vorherigen Vertex, um eine Kante zu erstellen
            mesh.edges.add(1)
            mesh.edges[-1].vertices = [i - 1, i]
    
    # Füge den Skin Modifier hinzu
    skin_modifier = obj.modifiers.new(name="Skin", type='SKIN')
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.modifier_apply({"object": obj}, modifier="Skin")

# Umrechne die Weltkoordinaten in Blender-Koordinaten
blender_coordinates = [wgs84_to_blender(coord) for coord in coordinates]

# Rufe die Funktion zum Erstellen der 3D-Form auf
create_shape(blender_coordinates)
