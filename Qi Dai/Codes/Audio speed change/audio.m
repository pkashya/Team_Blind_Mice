[d,sr]=audioread('10.mp3');
sr=44100;
% 1024 samples is about 60 ms at 16kHz, a good window
y=pvoc(d,2.0,1024);
% Compare original and resynthesis
%sound(d,44100)
sound(y,44100)
audiowrite('2test.wav', y, 44100)