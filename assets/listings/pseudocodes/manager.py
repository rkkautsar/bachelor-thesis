class BaseManager(object):
    def prepare(self):
        setup_tunneling()

    def spawn_workers(self):
        raise NotImplementedError

    def bootstrap(self):
        setup_sockets(...)
        config = bootstrap_client(self.config)
        payload = get_payload(config, ...)
        send_event(self.socket, BOOTSTRAP, payload)
        self.pending = decode_message(self.socket.recv())

    def wait(self):
        pass

    def stop(self):
        pass

    def run(self):
        self.prepare()
        self.bootstrap()
        self.spawn_workers()
        self.wait()
