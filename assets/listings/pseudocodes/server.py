class BenchmarkServer(object):
    def __init__(self, ..., **kwargs):
        initialize_db(...)

    def wait_for_bootstrap(self):
        while True:
            address, event_type, payload = self.frontend.recv_multipart()
            if event_type == BOOTSTRAP:
                break

        payload = decode_message(payload)
        bootstrap(**payload)
        self.frontend.send_multipart([address, b"done"])

    def loop(self):
        while True:
            address, event_type, payload = self.frontend.recv_multipart()
            self.backend.send_multipart([event_type, payload, address])

    def run(self):
        setup_sockets(...)

        self.wait_for_bootstrap()

        self.observers += [
            import_class(o.module) for o in Observer.select(Observer.module)
        ]
        observer_greenlets = []
        for observer in self.observers:
            greenlet = gevent.spawn(observer.observe)
            observer_greenlets.append(greenlet)

        serverlet = gevent.spawn(self.loop)
        serverlet.join()
        gevent.killall(observer_greenlets)
