//~ Final, experimental version
var shuffleSequence = seq("home", "intro", "fam", sepWith("sep", "pres"), "fam2", sepWith("sep", "practice"), "sexp", sepWith("sep", randomize("expe")), "endexpe");

//~ No sep
//~ var shuffleSequence = seq("home", "intro", "fam", seq("pres"), "fam2", seq("practice"), "sexp", seq(randomize("expe")));



//~ Only expe stim
//~ var shuffleSequence = seq(sepWith("sep", randomize("expe")));

var practiceMessage = "session de familiarisation";
var practiceItemTypes = ["practice", "practice2"];

var progressBarText = "progression";

completionMessage = "Vos r\u00e9ponses nous sont bien parvenues. \r\nMerci beaucoup pour le temps que vous nous avez offert. \r\nSi vous souhaitez des informations additionnelles, envoyez un message \u00e0 Lucas Tual \u00e0 l'adresse lucas.tual@unige.ch. \n Vous pouvez maintenant fermer cette fen\u00eatre!";

var defaults = [
    "Separator", {
        transfer: 1500,
        normalMessage: "Attendez la prochaine phrase.",
        errorMessage: "Wrong. Please wait for the next sentence."
    },
    "DashedSentence", {
        mode: "self-paced reading"
    },
    "AcceptabilityJudgment", {
        as: ["1", "2", "3", "4", "5", "6", "7"],
        presentAsScale: true,
        instructions: "Use number keys or click boxes to answer.",
        leftComment: "(Bad)", rightComment: "(Good)"
    },
    "Question", {
        hasCorrect: false,
		presentHorizontally: true,
		randomOrder: false
    },
    "Question2", {
        hasCorrect: false,
		presentHorizontally: false,
		randomOrder: false,
		showNumbers: false
    },
    "Message", {
        hideProgressBar: true
    },
    "Formit", {
        hideProgressBar: true,
        continueOnReturn: true,
        saveReactionTime: true
    }
];

var items = [

    // New in Ibex 0.3-beta-9. You can now add a '__SendResults__' controller in your shuffleOui
    // sequence to send results before the experiment has finished. This is NOT intended to allow
    // for incremental sending of results -- you should send results exactly once per experiment.
    // However, it does permit additional messages to be displayed to participants once the
    // experiment itself is over. If you are manually inserting a '__SendResults__' controller into
    // the shuffle sequence, you must set the 'manualSendResults' configuration variable to 'true', since
    // otherwise, results are automatically sent at the end of the experiment.
    //
    //["sr", "__SendResults__", { }],

    ["sep", "Separator", { }],

    // New in Ibex 0.3-beta19. You can now determine the point in the experiment at which the counter
    // for latin square designs will be updated. (Previously, this was always updated upon completion
    // of the experiment.) To do this, insert the special '__SetCounter__' controller at the desired
    // point in your running order. If given no options, the counter is incremented by one. If given
    // an 'inc' option, the counter is incremented by the specified amount. If given a 'set' option,
    // the counter is set to the given number. (E.g., { set: 100 }, { inc: -1 })
    //
    //["setcounter", "__SetCounter__", { }],

    // NOTE: You could also use the 'Message' controller for the experiment intro (this provides a simple
    // consent checkbox).

    ["home", "Formit", {
        html: { include: "home.html" },
        validators: {
            age: function (s) { if (s.match(/^\d+$/)) return true; else return "Bad value for \u2018age\u2019"; }
        }
    } ],
    ["intro", "Formit", {
        html: { include: "example_intro.html" },
        validators: {
            age: function (s) { if (s.match(/^\d+$/)) return true; else return "Bad value for \u2018age\u2019"; }
        }
    } ],
    ["fam", "Formit", {
        html: { include: "iniziofam.html" },
        validators: {
            age: function (s) { if (s.match(/^\d+$/)) return true; else return "Bad value for \u2018age\u2019"; }
        }
    } ],
    ["fam2", "Formit", {
        html: { include: "iniziofam2.html" },
        validators: {
            age: function (s) { if (s.match(/^\d+$/)) return true; else return "Bad value for \u2018age\u2019"; }
        }
    } ],
    ["sexp", "Formit", {
        html: { include: "inizioexp.html" },
        validators: {
            age: function (s) { if (s.match(/^\d+$/)) return true; else return "Bad value for \u2018age\u2019"; }
        }
    } ],
    ["endexpe", "Formit", {
        html: { include: "endexpe.html" },
        validators: {
            age: function (s) { if (s.match(/^\d+$/)) return true; else return "Bad value for \u2018age\u2019"; }
        }
    } ],

	//
	//Some presentation of stim
	//
	["pres", "Question2", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/Originals/PI-OR-042-pe-0-M-velo.mp3'type='audio/mpeg'></source></audio><br><br><br>Voici une phrase prononcée par un locuteur natif du français.<br><br><br></div>", as: ["Cliquez ici pour continuer"]}],
	["pres", "Question2", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/MBROLA-clair/PI-MC-042-pe-0-M-velo.mp3'type='audio/mpeg'></source></audio><br><br><br>Voici la même  phrase prononcée par une voix de synthèse.<br><br><br></div>", as: ["Cliquez ici pour continuer"]}],
	["pres", "Question2", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/MBROLA-delexicalised/PI-MD-042-pe-0-M-velo.mp3'type='audio/mpeg'></source></audio><br><br><br>Voici la même phrase que les précédentes mais qui a été mal synthétisée volontairement.<br><br><br></div>", as: ["Cliquez ici pour continuer"]}],
	
	
	
	//
	//Some practices
	//
	//~ ["practice", "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/Originals/PI-OR-041-pe-0-M-journee.mp3'type='audio/mpeg'></source></audio><br><br><br><br><br><br>Selon vous, est-ce que cette phrase pourrait être un ordre ?</div>", as: ["Oui", "Non"]}],
	["practice", "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/MBROLA-clair/PI-MC-041-pe-0-M-journee.mp3'type='audio/mpeg'></source></audio><br><br><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une phrase exclamative ?</div>", as: ["Oui", "Non"]}],
	//~ ["practice", "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/MBROLA-delexicalised/PI-MD-041-pe-0-M-journee.mp3'type='audio/mpeg'></source></audio><br><br><br><br><br><br>Selon vous, est-ce que cette phrase pourrait être un ordre ?</div>", as: ["Oui", "Non"]}],
	["practice", "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/Originals/PI-OR-043-pi-0-M-nedorspas.mp3'type='audio/mpeg'></source></audio><br><br><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	//~ ["practice", "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/MBROLA-delexicalised/PI-MD-043-pi-0-M-nedorspas.mp3'type='audio/mpeg'></source></audio><br><br><br><br><br><br>Selon vous, est-ce que cette phrase pourrait être une phrase exclamative ?</div>", as: ["Oui", "Non"]}],
	//~ ["practice", "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/MBROLA-clair/PI-MC-043-pi-0-M-nedorspas.mp3'type='audio/mpeg'></source></audio><br><br><br><br><br><br>Selon vous, est-ce que cette phrase pourrait être une phrase exclamative ?</div>", as: ["Oui", "Non"]}],
	//~ ["practice", "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/Originals/PI-OR-044-pi-0-M-melon.mp3'type='audio/mpeg'></source></audio><br><br><br><br><br><br>Selon vous, est-ce que cette phrase pourrait être une phrase exclamative ?</div>", as: ["Oui", "Non"]}],
	["practice", "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/MBROLA-delexicalised/PI-MD-044-pi-0-M-melon.mp3'type='audio/mpeg'></source></audio><br><br><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être un ordre ?</div>", as: ["Oui", "Non"]}],
	//~ ["practice", "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Practices/MBROLA-clair/PI-MC-044-pi-0-M-melon.mp3'type='audio/mpeg'></source></audio><br><br><br><br><br><br>Selon vous, est-ce que cette phrase pourrait être une phrase exclamative ?</div>", as: ["Oui", "Non"]}],
	

	//
	//Experimental stim
	//
	
	[["expe",1], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-001-de-0-M-WE2_A001_1952s875.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",1], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-001-de-0-M-WE2_A001_1952s875.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",2], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-002-yn-0-M-WE2_A001_6885.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",2], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-002-yn-0-M-WE2_A001_6885.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",3], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-004-de-0-F-WE2_A003_2972s210.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",3], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-004-de-0-F-WE2_A003_2972s210.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",4], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-005-de-0-F-WE2_A003_4686s24.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",4], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-005-de-0-F-WE2_A003_4686s24.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",5], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-008-yn-0-M-WE2_A005_206.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",5], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-008-yn-0-M-WE2_A005_206.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",6], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-009-de-0-F-WE2_A007_1541s511.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",6], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-009-de-0-F-WE2_A007_1541s511.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",7], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-010-yn-0-F-WE2_A007_4520.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",7], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-010-yn-0-F-WE2_A007_4520.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",8], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-011-yn-0-F-WE2_A007_917.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",8], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-011-yn-0-F-WE2_A007_917.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",9], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-012-de-0-F-WE2_A008_1238s554.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",9], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-012-de-0-F-WE2_A008_1238s554.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",10], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-013-de-0-F-WE2_A008_3247s562.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",10], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-013-de-0-F-WE2_A008_3247s562.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",11], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-015-de-0-F-WE2_A008_3922s864.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",11], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-015-de-0-F-WE2_A008_3922s864.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",12], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-016-de-0-F-WE2_A008_3984s177.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",12], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-016-de-0-F-WE2_A008_3984s177.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",13], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-017-de-0-M-WE2_A016_2716s551.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",13], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-017-de-0-M-WE2_A016_2716s551.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",14], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-018-yn-0-F-WE2_A018_3172.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",14], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-018-yn-0-F-WE2_A018_3172.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",15], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-020-yn-0-F-WE2_A020_6349.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",15], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-020-yn-0-F-WE2_A020_6349.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",16], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-022-de-0-F-WE2_A021_630s927.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",16], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-022-de-0-F-WE2_A021_630s927.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",17], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-023-yn-0-M-WE2_A021_6777.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",17], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-023-yn-0-M-WE2_A021_6777.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",18], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-025-yn-0-F-WE2_A025_3273.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",18], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-025-yn-0-F-WE2_A025_3273.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",19], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-027-yn-0-F-WE2_A025_8981.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",19], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-027-yn-0-F-WE2_A025_8981.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",20], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-028-yn-0-F-WE2_A025_9133.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",20], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/Originals/PI-OR-028-yn-0-F-WE2_A025_9133.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",21], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-003-wi-0-F-WE2_A003_2012.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",21], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/PI-MD-003-wi-0-F-WE2_A003_2012.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",22], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-014-wi-0-M-WE2_A008_3824.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",22], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/PI-MD-014-wi-0-M-WE2_A008_3824.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",23], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-019-wi-0-M-WE2_A019_1414.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",23], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/PI-MD-019-wi-0-M-WE2_A019_1414.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",24], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-021-wi-0-M-WE2_A021_5776.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",24], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/PI-MD-021-wi-0-M-WE2_A021_5776.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",25], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-029-wi-0-F-WE2_A031_7398.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",25], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/PI-MD-029-wi-0-F-WE2_A031_7398.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",26], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-030-wi-0-M-WE2_A046_1361.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",26], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/PI-MD-030-wi-0-M-WE2_A046_1361.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",27], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-031-wi-0-F-WE2_A062_4479.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",27], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/PI-MD-031-wi-0-F-WE2_A062_4479.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",28], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-032-wi-0-F-WE2_A064_98.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",28], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/PI-MD-032-wi-0-F-WE2_A064_98.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",29], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-035-wi-0-F-WE2_A069_2520.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",29], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/PI-MD-035-wi-0-F-WE2_A069_2520.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",30], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-clair/PI-MC-036-wi-0-F-WE2_A069_3246.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],
	[["expe",30], "Question", {q: "<div style=\"width: 40em;\"><audio autoplay controls preload=\"auto\"><source src='https://raw.githubusercontent.com/ltinsitu/EXP_perception_contours_finaux/master/PILOT_EXPE_Ibex/Audio/Expe_Stimuli/MBROLA-delexicalised/PI-MD-036-wi-0-F-WE2_A069_3246.mp3'type='audio/mpeg'></source></audio><br><br><br><br>Est-ce que cette phrase vous donne l'impression d'être une question ?</div>", as: ["Oui", "Non"]}],



];
