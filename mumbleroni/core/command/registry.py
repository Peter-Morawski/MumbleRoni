# -*- coding: utf-8 -*-

import logging
from mumbleroni.core.command.error import RegistrationError
from mumbleroni.settings.parser import SettingsParser

_logger = logging.getLogger(__name__)


class CommandRegistry:
    _command_queue = {}
    _commands = {}

    def __init__(self):
        self._settings = SettingsParser.parse()

    @classmethod
    def add_to_queue(cls, command, function):
        """
        Registers a command to the command queue.
        :param command: The name of the command.
        :param function: The function it will trigger.
        """
        _logger.debug("Adding command to queue.")

        if command in cls._command_queue.keys():
            raise RegistrationError("A command with the name {} already exists.".format(command))

        cls._command_queue[command] = function
        _logger.info("Successfully added the command: \"{}\" to the queue.".format(command))

    def register_queued_commands(self):
        """
        Registers all commands from the command queue.
        """
        _logger.debug("Registering queued commands.")

        for command_name in self._command_queue.keys():
            self._commands[command_name] = self._command_queue[command_name]

        self._command_queue.clear()
        _logger.info("Successfully registered queued commands.")

    def clear_queue(self):
        """
        Deletes all commands from the command queue.
        """
        _logger.debug("Unregistering queued commands.")
        self._command_queue.clear()

    @property
    def commands(self):
        return self._commands
