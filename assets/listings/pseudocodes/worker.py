class BenchmarkWorker:
    def __init__(self, ...):
        if use_tunneling:
            start_tunneling()

    def run(self):
        setup_sockets()

        send_event(self.socket, WORKER_JOIN)
        run = decode_message(self.socket.recv())

        tool = import_class(run["tool"])
        if not tool.is_ready():
            tool.setup()

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
        stop_tunneling()
