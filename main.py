import json
from nicegui import ui

# Konfiguration laden
def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "timers": [
                {"label": "30s", "duration": 30},
                {"label": "60s", "duration": 60},
                {"label": "120s", "duration": 120}
            ]
        }

config = load_config()

class WorkoutTimer:
    def __init__(self):
        self.seconds_left = 0
        self.total_duration = 0
        self.halfway_signal = False
        self.is_running = False
        self.timer = ui.timer(1.0, self.tick, active=False)
        self.halfway_played = False

        with ui.column().classes('w-full items-center p-8 gap-4'):
            ui.label('Gymnastik-Timer').classes('text-4xl font-bold mb-4')
            
            # Anzeige der verbleibenden Zeit
            self.label = ui.label('00:00').classes('text-6xl font-mono p-4 bg-gray-100 rounded-lg shadow-inner')

            # Auswahl für Signal zur Hälfte
            self.halfway_checkbox = ui.checkbox('Signal bei der Hälfte der Zeit').bind_value(self, 'halfway_signal')

            # Timer Buttons
            with ui.column().classes('gap-4 mt-4'):
                for t in config['timers']:
                    ui.button(t['label'], on_click=lambda t=t: self.start_timer(t['duration'])).classes('w-32 py-2')

            # Reset Button
            ui.button('Reset', on_click=self.reset, color='red').classes('w-32 mt-4')

    def play_sound(self):
        # Einfacher Piepton über Web Audio API
        ui.run_javascript('''
            var context = new (window.AudioContext || window.webkitAudioContext)();
            var oscillator = context.createOscillator();
            oscillator.type = 'sine';
            oscillator.frequency.setValueAtTime(440, context.currentTime);
            oscillator.connect(context.destination);
            oscillator.start();
            oscillator.stop(context.currentTime + 0.3);
        ''')

    def start_timer(self, duration):
        self.total_duration = duration
        self.seconds_left = duration
        self.halfway_played = False
        self.is_running = True
        self.update_display()
        self.timer.activate()
        # Kurzes Signal zum Start
        # self.play_sound() 

    def tick(self):
        if self.seconds_left > 0:
            self.seconds_left -= 1
            self.update_display()

            # Signal zur Hälfte prüfen
            if self.halfway_signal and not self.halfway_played:
                if self.seconds_left <= self.total_duration / 2:
                    self.play_sound()
                    self.halfway_played = True
                    ui.notify('Hälfte der Zeit erreicht!')

            # Signal am Ende
            if self.seconds_left == 0:
                self.play_sound()
                self.timer.deactivate()
                self.is_running = False
                ui.notify('Timer beendet!', type='positive')

    def update_display(self):
        minutes = self.seconds_left // 60
        seconds = self.seconds_left % 60
        self.label.set_text(f'{minutes:02d}:{seconds:02d}')

    def reset(self):
        self.timer.deactivate()
        self.seconds_left = 0
        self.is_running = False
        self.update_display()

@ui.page('/')
def main():
    WorkoutTimer()

ui.run(title='Gymnastik Workout Timer', native=False, host='0.0.0.0')
