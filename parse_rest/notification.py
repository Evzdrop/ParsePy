#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from installation import Push


class PushNotification(object):
    channels = None
    message = None
    sound = None
    where = None
    badge = None

    _data = None
    _kwargs = None

    def __init__(self, message=None, channels=[], sound=None, where={}, badge="Increment"):
        self.message = message
        self.channels = channels
        self.sound = sound
        self.where = where
        self.badge = badge
        self.expiration = None

        self._data = {'alert': message, 'badge': badge}
        self._kwargs = {}

    def send(self):
        self._prepare_push()
        Push.alert(self._data, self.where, **self._kwargs)

    def set_notification_expiration(self, date):
        #TODO Need to add logic to confirm ISO 8601 format (e.g. 2013-07-11T00:31:38Z)
        self._kwargs['expiration_time'] = date

    def _prepare_push(self):
        if self.sound:
            self._data['sound'] = self.sound

        if len(self.channels):
            self._kwargs['channels'] = self.channels
