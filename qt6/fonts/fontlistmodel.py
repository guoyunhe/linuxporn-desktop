import asyncio
from aiohttp import ClientSession

from PySide6.QtCore import Qt, QAbstractListModel, QByteArray, QObject, QThread, Signal, Slot


class FontListModel(QAbstractListModel):
    __data = [
        {
            'fontFamily': 'Noto Sans',
        },
        {
            'fontFamily': 'Noto Sans CJK',
        },
        {
            'fontFamily': 'Noto Sans',
        },
        {
            'fontFamily': 'Noto Sans CJK',
        },
        {
            'fontFamily': 'Noto Sans',
        },
        {
            'fontFamily': 'Noto Sans CJK',
        },
        {
            'fontFamily': 'Noto Sans',
        },
        {
            'fontFamily': 'Noto Sans CJK',
        },
        {
            'fontFamily': 'Noto Sans',
        },
        {
            'fontFamily': 'Noto Sans CJK',
        },
        {
            'fontFamily': 'Noto Sans',
        },
        {
            'fontFamily': 'Noto Sans CJK',
        },
        {
            'fontFamily': 'Noto Sans',
        },
        {
            'fontFamily': 'Noto Sans CJK',
        },
        {
            'fontFamily': 'Noto Sans',
        },
        {
            'fontFamily': 'Noto Sans CJK',
        },
        {
            'fontFamily': 'Noto Sans',
        },
        {
            'fontFamily': 'Noto Sans CJK',
        },
        {
            'fontFamily': 'Noto Sans',
        },
        {
            'fontFamily': 'Noto Sans CJK',
        },
        {
            'fontFamily': 'Noto Sans',
        },
        {
            'fontFamily': 'Noto Sans CJK',
        },
    ]

    def __init__(self, parent=None):
        super().__init__(parent)

    def roleNames(self):
        return {
            0: b'fontFamily'
        }

    def rowCount(self, index):
        return len(self.__data)

    def data(self, index, role):
        d = self.__data[index.row()]

        if role == 0:
            return d['fontFamily']

        return d

    def populate(self, data=None):
        for item in data:
            self.__data.append(item)
