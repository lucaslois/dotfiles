import os
import shutil

backupDirectory = "./.config"
filesToBackup = [
	"/home/lucasl/.config/i3",
	"/home/lucasl/.config/i3blocks",
	"/home/lucasl/.config/i3status",
	"/home/lucasl/.config/rofi",
	"/home/lucasl/.config/configsaver.sh",
	"/home/lucasl/.zshrc",
	"/home/lucasl/.vimrc"
]

def createFolder(path):
	print("Creating directory in \"{}\"".format(path))
	try:
		os.mkdir(path)
	except FileExistsError:
		print("Already exists a folder named {}".format(path))	

def deleteFolder(path):
	shutil.rmtree(path)
	print("Directory \"{}\" deleted successfuly".format(path))

def copyFilesToBackupFolder(pathList):
	for path in pathList:
		folders = path.split('/')
		lastFolder = folders[-1]
		
		if not os.path.exists(path):
			print("Path \"{}\" does not exist".format(path))
			continue

		if os.path.isfile(path):
			shutil.copy(path, backupDirectory)
		else:
			destDirectory = "{}/{}".format(backupDirectory, lastFolder)
			shutil.copytree(path, destDirectory, dirs_exist_ok=True)

def main():
	createFolder(backupDirectory)
	copyFilesToBackupFolder(filesToBackup)

	# deleteFolder()

main()