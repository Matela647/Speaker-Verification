import numpy as np
import joblib
import sys

# Get the callerID argument passed from the command line
if len(sys.argv) < 2:
    print("Error: Missing callerID argument.")
    sys.exit(1)

callerID = str(sys.argv[1])  # Convert the argument to a string

# Load the saved features
savePath = f'/home/setenane/Desktop/SV_for_Password_Reset/Verification_features/{callerID}.dat'
allMFCCs = np.loadtxt(savePath)

# Load the universal background model
ubmModelPath = '/home/setenane/Desktop/SV_for_Password_Reset/Universal_Background_Model/GMM_UBM.pkl'
ubmGmm = joblib.load(ubmModelPath)

# Load the user-specific model
userModelPath = f'/home/setenane/Desktop/SV_for_Password_Reset/User_models/{callerID}.pkl'
userGmm = joblib.load(userModelPath)

# Perform speaker verification
ubmScores = ubmGmm.score_samples(allMFCCs.T)
userScores = userGmm.score_samples(allMFCCs.T)

# Set a threshold for verification
threshold = -1
verification = 0

difference = userScores.mean() - ubmScores.mean()

if difference > threshold:
    verification = 1
else:
    verification = 0

if verification == 1:
    print(difference)
    print("Speaker is Verified")
else:
    print(difference)
    print("Verification failed")
    


