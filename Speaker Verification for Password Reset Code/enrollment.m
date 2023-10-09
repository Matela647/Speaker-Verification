function enrollment(callerID)
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
    audioDir = ['/home/setenane/Desktop/SV_for_Password_Reset/enrollment/', callerID];

    % List all audio files in the directory
    audioFiles = dir(fullfile(audioDir, '*.wav'));

    % Initialize a matrix to store MFCC features
    allMFCCs = [];

    % Loop through each audio file
    for i = 1:length(audioFiles)
        % Construct the full path to the audio file
        filePath = fullfile(audioDir, audioFiles(i).name);

        % Read speech samples and sampling rate from the file
        [speech, fs] = audioread(filePath);

        % Feature extraction
        [MFCCs, ~, ~] = mfcc(speech, fs, Tw, Ts, alpha, @hamming, [LF HF], M, C+1, L);

        % Append the extracted MFCCs to the matrix
        allMFCCs = [allMFCCs, MFCCs];
    end

    % Save the extracted features to a plain text file with .dat extension
    savePath = ['/home/setenane/Desktop/SV_for_Password_Reset/Enrollment_features/', callerID, '.dat'];
    dlmwrite(savePath, allMFCCs, ' ');

    disp('Feature extraction and saving completed.');

end

