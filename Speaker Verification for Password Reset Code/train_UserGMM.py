import numpy as np
from sklearn.mixture import GaussianMixture
import joblib
import sys

# Get the callerID argument passed from the command line
if len(sys.argv) < 2:
    print("Error: Missing callerID argument.")
    sys.exit(1)

callerID = str(sys.argv[1])  # Convert the argument to a string

# Load the saved features
savePath = f'/home/setenane/Desktop/SV_for_Password_Reset/Enrollment_features/{callerID}.dat'
allMFCCs = np.loadtxt(savePath)

# Train a Gaussian Mixture Model
gmm = GaussianMixture(n_components=64, covariance_type='diag', random_state=0)
gmm.fit(allMFCCs.T)

# Save the trained model
modelPath = f'/home/setenane/Desktop/SV_for_Password_Reset/User_models/{callerID}.pkl'
joblib.dump(gmm, modelPath)

# Store the enrollment result in a variable
ENROLLMENT_RESULT = 'Enrolled Successfully'

# Remove leading and trailing whitespace
ENROLLMENT_RESULT = ENROLLMENT_RESULT.strip()

# Print the enrollment result
print(ENROLLMENT_RESULT)

# Return the enrollment result to the dialplan
sys.stdout.flush()

