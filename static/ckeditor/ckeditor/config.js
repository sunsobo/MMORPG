/**
 * @license Copyright (c) 2003-2023, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	config.disableNativeSpellChecker = false;
	config.removePlugins = 'contextmenu,liststyle,tabletools,tableselection';
	config.extraPlugins = 'youtube';
	config.youtube_autoplay = false;
	config.youtube_controls = true;
	//config.youtube_width = '300';
	//config.youtube_height = '200';

	config.image_toolbar = 'link';

// 	config.enterMode = CKEDITOR.ENTER_BR;

	//config.smiley_images = ['smile.png',];
    //config.smiley_descriptions = ['smiley', ];
};