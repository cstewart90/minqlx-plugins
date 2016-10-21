# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# If you have any suggestions or issues/problems with this plugin you can contact me(kanzo) on irc at #minqlbot
# or alternatively you can open an issue at https://github.com/cstewart90/minqlx-plugins/issues

"""
Removes powerups on round end. Mainly used for freezetag because `g_freezeRemovePowerupsOnRound`
doesn't remove powerups right away.
"""

import minqlx


class removepowerups(minqlx.Plugin):
    def __init__(self):
        super().__init__()
        self.add_hook("round_end", self.handle_round_end)

    def handle_round_end(self, data):
        """Removes all powerups on round end."""
        for p in self.players():
            p.powerups(reset=True)
