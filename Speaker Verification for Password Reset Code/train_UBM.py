import numpy as np
from sklearn.mixture import GaussianMixture
import joblib

# Load the saved features
savePath = '/home/setenane/Desktop/SV_for_Password_Reset/UBM_training/UBM_GMM.dat'
allMFCCs = np.loadtxt(savePath)

# Train a Gaussian Mixture Model
gmm = GaussianMixture(n_components=64, covariance_type='diag', random_state=0)
gmm.fit(allMFCCs.T)

# Save the trained model
modelPath = '/home/setenane/Desktop/SV_for_Password_Reset/Universal_Background_Model/GMM_UBM.pkl'
joblib.dump(gmm, modelPath)


