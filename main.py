import sys
import cv2 as cv
import niproc


# Check if there is any input to be read
if len(sys.argv) is 1:
    print("USAGE: shape-detection.py [file1] (file2) (file3)...")
    print("OR:    shape-detection.py -v (device)")
    print("No files specified, exiting")

# User requested we use video input.
if sys.argv[1] is "-v":
    # Find which device was specified by user, or default to device 0
    if len(sys.argv) > 2:
        cap = cv.VideoCapture(sys.argv[2])
    else:
        cap = cv.VideoCapture(0)

    # Do video interpretation until process is killed
    while True:
        ret, frame = cap.read()
        pimg = niproc.processimage(frame)

# There's input, read it!
for uin in sys.argv[1:]:
    print("Loading ", uin)
    img = cv.imread(uin)

    if img is not None:
        print("Found image")

        # TODO: Do interpretation stuff here to Processed IMaGe (pimg)
        pimg = img
        pimg = niproc.processimage(pimg)
        pimg = cv.pyrDown(pimg)

        cv.imshow("Current image", pimg)
        cv.waitKey()
        cv.destroyAllWindows()

    else:
        print("Couldn't read that file. Does it exist at the location specified?")

