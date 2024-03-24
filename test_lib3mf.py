import Lib3MF
from Lib3MF import get_wrapper


def buildTriangle(mesh):
	triangle = Lib3MF.Triangle()
	position = Lib3MF.Position()

	position.Coordinates[0] = 0
	position.Coordinates[1] = 0
	position.Coordinates[2] = 0
	triangle.Indices[0] = mesh.AddVertex(position)

	position.Coordinates[0] = 0
	position.Coordinates[1] = 1
	position.Coordinates[2] = 0
	triangle.Indices[1] = mesh.AddVertex(position)

	position.Coordinates[0] = 0
	position.Coordinates[1] = 0
	position.Coordinates[2] = 1
	triangle.Indices[2] = mesh.AddVertex(position)

	mesh.AddTriangle(triangle)

def main():
	# Get the wrapper
	wrapper = get_wrapper()
	
	major, minor, micro = wrapper.GetLibraryVersion()
	print("Lib3MF version: {:d}.{:d}.{:d}".format(major, minor, micro), end="")
	hasInfo, prereleaseinfo = wrapper.GetPrereleaseInformation()
	if hasInfo:
		print("-"+prereleaseinfo, end="")
	hasInfo, buildinfo = wrapper.GetBuildInformation()
	if hasInfo:
		print("+"+buildinfo, end="")
	print("")
	# this example is REALLY simplisitic, but you get the point :)
	model = wrapper.CreateModel()
	meshObject = model.AddMeshObject()
	buildTriangle(meshObject)
	writer = model.QueryWriter("3mf")
	writer.WriteToFile("triangle.3mf")

if __name__ == "__main__":
	try:
		main()
	except Lib3MF.ELib3MFException as e:
		print(e)