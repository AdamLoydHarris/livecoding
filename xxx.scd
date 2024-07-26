Platform.userExtensionDir


s.boot;
s.pause;
s.quit;



s.options.numInputBusChannels = 0;  // Disable input channels

Server.default.options.numInputBusChannels = 0;




{ SinOsc.ar(XLine.kr(1000, 110), 0, 0.3) }.play;
{
	[SinOsc.ar(310, 1, 0.2), SinOsc.ar(547, 0, 0.2)] }.play;



(
s.waitForBoot {
    ~dirt = SuperDirt(2, s); // 2 output channels, you can adjust as needed
    ~dirt.loadSoundFiles;    // Load default samples
    s.sync;                  // Wait for synchronization
    ~dirt.start(57120, 0 ! 12); // Start SuperDirt on port 57120
};
)


SuperDirt()
SuperDirt.start;


s.sync;
SuperDirt.synths.keys.do { |synth| s.postln(synth) };

s.sync;

SuperDirt.allSamples.do { |sample| s.postln(sample) };


~dirt.loadSoundFiles("/Users/AdamHarris/Library/Application Support/SuperCollider/downloaded-quarks/samples-extra/*");


s.quit;  // Stops the server
s.reboot;  // Reboots the server, clearing a