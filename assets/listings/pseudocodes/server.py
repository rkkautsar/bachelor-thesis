class BenchmarkServer(object):
    def receive_event(self):
        address, event_type, payload = self.frontend.recv_multipart()
        return address, event_type, payload

    def loop(self):
        while True:
            address, event_type, payload = self.receive_event()
            self.backend.send_multipart([event_type, payload, address])

    def run(self):
        setup_sockets(...)  # self.frontend and self.backend

        core_observer_greenlet = gevent.spawn(CoreObserver.observe, ...)
        serverlet = gevent.spawn(self.loop)
        serverlet.join()
        core_observer_greenlet.kill()
