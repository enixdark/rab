import sys, json, httplib, base64

if __name__ == "__main__":
	status = sys.argv[1]
	if status.lower() == "warning":
		print "Status is WARN"
		exit(1)
	elif status.lower() == "critical":
		print "Status is CRITICAL"
		exit(2)
	elif status.lower() == "unknown":
		print "Status is UNKNOWN"
		exit(3)
	else:
		print "Status is OK"
		exit(0)