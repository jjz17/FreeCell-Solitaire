class TextView:
    def __init__(self, model):
        self.model = model

    def render_board(self):
        return str(self.model)