from midiutil import MIDIFile

# Parametri per il file MIDI
midi = MIDIFile(1)  # Un'unica traccia
track = 0
tempo = 90  # Imposta il tempo della musica
midi.addTempo(track, 0, tempo)

# Funzione per aggiungere una sequenza melodica per "Quasi" e un accompagnamento per "Quanto"
def aggiungi_sequenza_quasi_quanto(midi, track, start_time=0, durata_quasi=1, durata_quanto=2):
    # Quasi: sequenza di note ondulanti
    quasi_notes = [60, 62, 64, 65, 67, 65, 64, 62]  # Serie melodica che "oscilla"
    for i, note in enumerate(quasi_notes):
        midi.addNote(track, 0, note, start_time + i * durata_quasi, durata_quasi, 100)  # Aggiunge ogni nota di Quasi

    # Quanto: note più stabili e ripetitive come accompagnamento armonico
    quanto_notes = [48, 52, 55, 52]  # Basso armonico
    for j in range(4):  # Ripetere per coprire la stessa lunghezza di Quasi
        for note in quanto_notes:
            midi.addNote(track, 1, note, start_time + j * len(quasi_notes) * durata_quanto, durata_quanto, 80)  # Quanto più stabile

# Aggiungere sequenza musicale
aggiungi_sequenza_quasi_quanto(midi, track)

# Salvare il file MIDI
with open("Questa_e_Quanto_musica.mid", "wb") as output_file:
    midi.writeFile(output_file)