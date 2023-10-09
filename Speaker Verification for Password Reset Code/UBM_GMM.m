% Define variables
Tw = 25;                % analysis frame duration (ms)
Ts = 10;                % analysis frame shift (ms)
alpha = 0.97;           % preemphasis coefficient
M = 20;                 % number of filterbank channels 
C = 12;                 % number of cepstral coefficients
L = 22;                 % cepstral sine lifter parameter
LF = 300;               % lower frequency limit (Hz)
HF = 3700;              % upper frequency limit (Hz)

% Set the directory containing the audio files
rootDir = '/home/setenane/Desktop/SV_for_Password_Reset/UBM_training';

% Initialize a matrix to store MFCC features
allMFCCs = [];

% Recursively search for all .wav files in sub-folders
audioFiles = dir(fullfile(rootDir, '**', '*.wav'));

% Loop through each audio file
for i = 1:length(audioFiles)
    % Construct the full path to the audio file
    filePath = fullfile(audioFiles(i).folder, audioFiles(i).name);

    % Read speech samples and sampling rate from the file
    [speech, fs] = audioread(filePath);

    % Feature extraction
    [MFCCs, ~, ~] = mfcc(speech, fs, Tw, Ts, alpha, @hamming, [LF HF], M, C+1, L);
    
    % Append the extracted MFCCs to the matrix
    allMFCCs = [allMFCCs, MFCCs];  % Use comma to concatenate columns
end

% Save the extracted features to a plain text file with .dat extension
savePath = '/home/setenane/Desktop/SV_for_Password_Reset/UBM_training/UBM_GMM.dat';
dlmwrite(savePath, allMFCCs, ' ');

disp('Feature extraction and saving completed.');

% EOF

