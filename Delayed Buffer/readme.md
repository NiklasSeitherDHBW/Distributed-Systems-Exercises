# Übung - Nebenläufigkeit in Python

Implementieren Sie einen einfachen `DelayedBuffer`, der es ermöglicht Aufgaben (d. h. Objekte vom Typ `Callable`) erst nach einer bestimmten Zeit auszuführen. Die Klasse muss zwei Funktionen zur Verfügung stellen:

```python
submit(self, delay, fn, *args, **kwargs):
    """
    Die Funktion fn wird nach delay Sekunden ausgeführt wobei delay vom Typ Float ist.
    args und kwargs sind die Argumente, die an fn übergeben werden.
    """

join(self):
    """
    Wartet bis alle Aufgaben abgearbeitet wurden.
    """
```

Im folgenden sehen Sie eine mögliche Verwendung des Puffers:

```python
buffer = DelayedBuffer()
buffer.submit(100 / 1000, ts_print, "Hello ", **{"end": "", "flush": True})
buffer.submit(1000 / 1000, ts_print, "World!")
buffer.submit(500 / 1000, ts_print, "of the ", **{"end": "", "flush": True})
buffer.submit(200 / 1000, ts_print, "from ", **{"end": "", "flush": True})
buffer.submit(300 / 1000, ts_print, "the other side ", **{"end": "", "flush": True})
# ggf. await buffer.join() im Falle von Koroutinen
buffer.join()
print("Done.")
```

### Implementation mit Threads
Implementieren Sie die Klasse `DelayedBuffer` mit Hilfe von Threads (und ggf. `Queues` bzw. Locks).  
Implementieren Sie `ts_print` als Thread-sichere Variante von `print`.

### Implementation mit Threadpool
Implementieren Sie die Klasse `DelayedBuffer` mit Hilfe eines `concurrent.futures.ThreadPool` (und
ggf. `Queues` bzw. Locks).  
Implementieren Sie `ts_print` als Thread-sichere Variante von print. Wählen Sie ggf. eine andere
Implementierung als in der vorherigen Aufgabe.

### Implementation mit Koroutinen
Implementieren Sie die Klasse `DelayBuffer` mit Hilfe von Korutinen (und ggf. `asyncio.Queues`).