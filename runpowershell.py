import subprocess
subprocess.Popen(["powershell.exe", "-NoExit", "python -m Scripts.label_image --graph=tf_files/retrained_graph.pb --image=tf_files\colon_cancer\Tumor.jpeg"])
