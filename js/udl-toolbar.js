/* ============================================================================
   UDL Toolbar — Universal Design for Learning Controls
   Vanilla JavaScript (no dependencies)
   ============================================================================ */

(function() {
  'use strict';

  /* ========================================================================
     CONFIG
     ======================================================================== */

  var CONFIG = {
    KEYS: {
      fontSize: 'udl-font-size',
      lineSpacing: 'udl-line-spacing',
      dyslexia: 'udl-dyslexia',
      mode: 'udl-mode',
      focusMode: 'udl-focus-mode'
    },
    DEFAULTS: {
      fontSize: 'default',
      lineSpacing: 'normal',
      dyslexia: 'false',
      mode: 'dark',
      focusMode: 'false'
    },
    FONT_CLASSES: ['udl-font-sm', 'udl-font-lg', 'udl-font-xl'],
    MODE_CLASSES: ['udl-light-mode', 'udl-high-contrast']
  };

  /* ========================================================================
     STATE
     ======================================================================== */

  var STATE = {
    currentSettings: {}
  };

  /* ========================================================================
     CORE FUNCTIONS
     ======================================================================== */

  function loadSettings() {
    var settings = CONFIG.DEFAULTS;
    try {
      for (var key in CONFIG.KEYS) {
        if (CONFIG.KEYS.hasOwnProperty(key)) {
          var stored = localStorage.getItem(CONFIG.KEYS[key]);
          settings[key] = stored !== null ? stored : CONFIG.DEFAULTS[key];
        }
      }
    } catch(e) {
      // localStorage not available, use defaults
    }
    STATE.currentSettings = settings;
    return settings;
  }

  function applySettings() {
    var h = document.documentElement;
    var settings = STATE.currentSettings;

    // Font size classes
    CONFIG.FONT_CLASSES.forEach(function(cls) {
      h.classList.remove(cls);
    });
    if (settings.fontSize && settings.fontSize !== 'default') {
      h.classList.add('udl-font-' + settings.fontSize);
    }

    // Line spacing
    h.classList.toggle('udl-line-relaxed', settings.lineSpacing === 'relaxed');

    // Dyslexia font
    h.classList.toggle('udl-dyslexia', settings.dyslexia === 'true');

    // Display mode
    CONFIG.MODE_CLASSES.forEach(function(cls) {
      h.classList.remove(cls);
    });
    if (settings.mode && settings.mode !== 'dark') {
      var modeClass = settings.mode === 'light' ? 'udl-light-mode' : 'udl-high-contrast';
      h.classList.add(modeClass);
    }

    // Focus mode
    h.classList.toggle('udl-focus-mode', settings.focusMode === 'true');
  }

  function saveSettings() {
    var settings = STATE.currentSettings;
    try {
      for (var key in CONFIG.KEYS) {
        if (CONFIG.KEYS.hasOwnProperty(key)) {
          localStorage.setItem(CONFIG.KEYS[key], settings[key]);
        }
      }
    } catch(e) {
      // localStorage not available, silently fail
    }
  }

  function setSetting(key, value) {
    STATE.currentSettings[key] = value;
    applySettings();
    saveSettings();
    updateAriaPressed();
  }

  /* ========================================================================
     TOOLBAR FUNCTIONS
     ======================================================================== */

  function initToggle() {
    var toggle = document.getElementById('udl-toolbar-toggle');
    var panel = document.getElementById('udl-toolbar-panel');

    if (!toggle || !panel) return;

    toggle.addEventListener('click', function() {
      var isExpanded = toggle.getAttribute('aria-expanded') === 'true';
      if (isExpanded) {
        closeToolbar();
      } else {
        openToolbar();
      }
    });
  }

  function openToolbar() {
    var toggle = document.getElementById('udl-toolbar-toggle');
    var panel = document.getElementById('udl-toolbar-panel');
    if (!toggle || !panel) return;

    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Close accessibility toolbar');
    panel.removeAttribute('hidden');
  }

  function closeToolbar() {
    var toggle = document.getElementById('udl-toolbar-toggle');
    var panel = document.getElementById('udl-toolbar-panel');
    if (!toggle || !panel) return;

    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open accessibility toolbar');
    panel.setAttribute('hidden', '');
  }

  function announce(msg) {
    var live = document.getElementById('udl-announce');
    if (!live) return;
    live.textContent = msg;
    // Clear after announcement is read
    setTimeout(function() {
      live.textContent = '';
    }, 3000);
  }

  function updateAriaPressed() {
    var buttons = document.querySelectorAll('[data-udl-action]');
    var settings = STATE.currentSettings;

    buttons.forEach(function(btn) {
      var action = btn.getAttribute('data-udl-action');
      var pressed = false;

      if (action === 'font-default') {
        pressed = settings.fontSize === 'default';
      } else if (action === 'font-sm') {
        pressed = settings.fontSize === 'sm';
      } else if (action === 'font-lg') {
        pressed = settings.fontSize === 'lg';
      } else if (action === 'font-xl') {
        pressed = settings.fontSize === 'xl';
      } else if (action === 'line-spacing') {
        pressed = settings.lineSpacing === 'relaxed';
      } else if (action === 'dyslexia') {
        pressed = settings.dyslexia === 'true';
      } else if (action === 'mode-dark') {
        pressed = settings.mode === 'dark';
      } else if (action === 'mode-light') {
        pressed = settings.mode === 'light';
      } else if (action === 'mode-hc') {
        pressed = settings.mode === 'hc';
      } else if (action === 'focus-mode') {
        pressed = settings.focusMode === 'true';
      }

      btn.setAttribute('aria-pressed', pressed ? 'true' : 'false');
    });
  }

  /* ========================================================================
     ACTION HANDLERS
     ======================================================================== */

  function handleFontSize(size) {
    setSetting('fontSize', size);
    var sizeNames = {
      sm: 'Small',
      default: 'Default',
      lg: 'Large',
      xl: 'Extra large'
    };
    announce('Font size set to ' + (sizeNames[size] || size));
  }

  function handleLineSpacing() {
    var current = STATE.currentSettings.lineSpacing;
    var newVal = current === 'relaxed' ? 'normal' : 'relaxed';
    setSetting('lineSpacing', newVal);
    announce('Line spacing ' + (newVal === 'relaxed' ? 'increased' : 'reset'));
  }

  function handleDyslexia() {
    var current = STATE.currentSettings.dyslexia;
    var newVal = current === 'true' ? 'false' : 'true';
    setSetting('dyslexia', newVal);
    announce('Dyslexia-friendly font ' + (newVal === 'true' ? 'enabled' : 'disabled'));
  }

  function handleMode(mode) {
    setSetting('mode', mode);
    var modeNames = {
      dark: 'Dark',
      light: 'Light',
      hc: 'High contrast'
    };
    announce('Display mode changed to ' + (modeNames[mode] || mode));
  }

  function handleFocusMode() {
    var current = STATE.currentSettings.focusMode;
    var newVal = current === 'true' ? 'false' : 'true';
    setSetting('focusMode', newVal);
    announce('Focus mode ' + (newVal === 'true' ? 'enabled' : 'disabled'));
  }

  /* ========================================================================
     TEXT-TO-SPEECH MODULE
     ======================================================================== */

  var TTS = {
    isSupported: function() {
      return !!window.speechSynthesis;
    },

    speak: function(text) {
      if (!this.isSupported()) return;
      window.speechSynthesis.cancel(); // Stop any ongoing speech
      var utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 1;
      utterance.pitch = 1;
      utterance.volume = 1;

      var stopBtn = document.querySelector('[data-udl-action="tts-stop"]');
      if (stopBtn) {
        stopBtn.setAttribute('aria-disabled', 'false');
      }

      utterance.onend = function() {
        if (stopBtn) {
          stopBtn.setAttribute('aria-disabled', 'true');
        }
        announce('Text-to-speech finished');
      };

      utterance.onerror = function(e) {
        announce('Text-to-speech error: ' + e.error);
      };

      window.speechSynthesis.speak(utterance);
      announce('Reading text');
    },

    readSelection: function() {
      var selected = window.getSelection().toString().trim();
      if (!selected) {
        announce('No text selected');
        return;
      }
      this.speak(selected);
    },

    readPage: function() {
      var main = document.getElementById('main-content');
      var text = main ? main.innerText : document.body.innerText;
      if (!text.trim()) {
        announce('No content to read');
        return;
      }
      this.speak(text);
    },

    stop: function() {
      if (!this.isSupported()) return;
      window.speechSynthesis.cancel();
      var stopBtn = document.querySelector('[data-udl-action="tts-stop"]');
      if (stopBtn) {
        stopBtn.setAttribute('aria-disabled', 'true');
      }
      announce('Reading stopped');
    }
  };

  /* ========================================================================
     BUTTON EVENT HANDLING
     ======================================================================== */

  function initButtons() {
    document.addEventListener('click', function(e) {
      var btn = e.target.closest('[data-udl-action]');
      if (!btn) return;

      e.preventDefault();
      var action = btn.getAttribute('data-udl-action');

      if (action === 'font-sm') {
        handleFontSize('sm');
      } else if (action === 'font-default') {
        handleFontSize('default');
      } else if (action === 'font-lg') {
        handleFontSize('lg');
      } else if (action === 'font-xl') {
        handleFontSize('xl');
      } else if (action === 'line-spacing') {
        handleLineSpacing();
      } else if (action === 'dyslexia') {
        handleDyslexia();
      } else if (action === 'mode-dark') {
        handleMode('dark');
      } else if (action === 'mode-light') {
        handleMode('light');
      } else if (action === 'mode-hc') {
        handleMode('hc');
      } else if (action === 'focus-mode') {
        handleFocusMode();
      } else if (action === 'tts-selection') {
        TTS.readSelection();
      } else if (action === 'tts-page') {
        TTS.readPage();
      } else if (action === 'tts-stop') {
        TTS.stop();
      }
    });
  }

  /* ========================================================================
     KEYBOARD SHORTCUTS
     ======================================================================== */

  function initKeyboard() {
    document.addEventListener('keydown', function(e) {
      // Don't capture when user is typing in a form
      var tag = document.activeElement && document.activeElement.tagName;
      if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
      if (document.activeElement && document.activeElement.isContentEditable) return;

      if (!e.altKey) {
        // Escape key closes toolbar
        if (e.key === 'Escape') {
          var panel = document.getElementById('udl-toolbar-panel');
          if (panel && !panel.hasAttribute('hidden')) {
            closeToolbar();
            document.getElementById('udl-toolbar-toggle').focus();
          }
        }
        return;
      }

      // Alt+key shortcuts
      switch (e.key.toLowerCase()) {
        case 'u':
          e.preventDefault();
          var toggle = document.getElementById('udl-toolbar-toggle');
          var isExpanded = toggle && toggle.getAttribute('aria-expanded') === 'true';
          if (isExpanded) closeToolbar();
          else openToolbar();
          toggle && toggle.focus();
          break;
        case '1':
          e.preventDefault();
          handleFontSize('sm');
          break;
        case '2':
          e.preventDefault();
          handleFontSize('default');
          break;
        case '3':
          e.preventDefault();
          handleFontSize('lg');
          break;
        case '4':
          e.preventDefault();
          handleFontSize('xl');
          break;
        case 'l':
          e.preventDefault();
          handleLineSpacing();
          break;
        case 'd':
          e.preventDefault();
          handleDyslexia();
          break;
        case '5':
          e.preventDefault();
          handleMode('dark');
          break;
        case '6':
          e.preventDefault();
          handleMode('light');
          break;
        case '7':
          e.preventDefault();
          handleMode('hc');
          break;
        case 'f':
          e.preventDefault();
          handleFocusMode();
          break;
        case 'r':
          e.preventDefault();
          TTS.readSelection();
          break;
        case 'p':
          e.preventDefault();
          TTS.readPage();
          break;
        case 's':
          e.preventDefault();
          TTS.stop();
          break;
      }
    });
  }

  /* ========================================================================
     INITIALIZATION
     ======================================================================== */

  function init() {
    // Load and apply saved preferences
    loadSettings();
    applySettings();

    // Hide TTS controls if not supported
    if (!TTS.isSupported()) {
      var ttsBtns = document.querySelectorAll('[data-udl-action^="tts-"]');
      ttsBtns.forEach(function(btn) {
        btn.setAttribute('aria-disabled', 'true');
      });
    }

    // Wire up toolbar
    initToggle();
    initButtons();
    initKeyboard();
    updateAriaPressed();
  }

  // Run after DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
