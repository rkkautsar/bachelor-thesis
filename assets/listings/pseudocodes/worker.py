class BenchmarkWorker:
    def killed(self, run_id):
        send_event(self.socket, RUN_INTERRUPT, run_id)
        send_event(self.socket, WORKER_LEAVE)

    def run(self):
        atexit.register(self.killed, self.run_id)

        context = zmq.Context()
        self.socket = context.socket(zmq.DEALER)
        self.socket.connect(self.server_address)

        send_event(self.socket, WORKER_JOIN, self.run_id)
        run = decode_message(self.socket.recv())

        tool = import_class(run["tool"])
        context = setup_context(...)
        create_run_directory(...)

        payload = dict(tool_version=tool.version(), run_id=self.run_id)
        send_event(self.socket, RUN_START, payload)

        for runstep in run["steps"]:
            step = import_class(runstep["module"])
            config = json.loads(runstep["config"])
            step.execute(context, config)
            payload = {"run_id": self.run_id, "step": runstep["module"]}
            send_event(self.socket, RUN_STEP, payload)

        send_event(self.socket, RUN_FINISH, self.run_id)
        send_event(self.socket, WORKER_LEAVE, self.run_id)
