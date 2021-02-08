import os
import shutil
import datetime

backupDirectory = "./dotfiles"
filesToBackup = [
	"/home/lucasl/.config/i3",
	"/home/lucasl/.config/i3blocks",
	"/home/lucasl/.config/i3status",
	"/home/lucasl/.config/rofi",
	"/home/lucasl/.config/configsaver.sh",
	"/home/lucasl/.zshrc",
	"/home/lucasl/.vimrc",
	"/home/lucasl/.tmux.conf",
]

def createFolder(path):
	print("Creating directory in \"{}\"".format(path))
	try:
		os.mkdir(path)
	except FileExistsError:
		print("Already exists a folder named {}".format(path))	

def deleteFolder(path):
	try:
		shutil.rmtree(path)
	except FileNotFoundError:
		return

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

			try:
				shutil.rmtree("{}/.git".format(destDirectory))
			except FileNotFoundError:
				continue	

def commitAndPush():
	today = datetime.datetime.now()
	os.system("git add .")
	os.system("git commit -m 'Updated at {}'".format(today))
	os.system("git push")

def main():
	deleteFolder(backupDirectory)
	createFolder(backupDirectory)
	copyFilesToBackupFolder(filesToBackup)
	commitAndPush()

	

main()