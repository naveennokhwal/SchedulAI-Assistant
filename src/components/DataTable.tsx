import React from 'react';

interface DataTableProps {
  data: [string, string, string, string][];
  type: 'tasks' | 'alarms' | 'reminders';
}

export function DataTable({ data, type }: DataTableProps) {
  return (
    <div className="bg-gray-800 rounded-lg overflow-hidden mb-4">
      <table className="w-full text-gray-100">
        <thead className="bg-gray-700">
          <tr>
            <th className="px-4 py-2 text-left">#</th>
            <th className="px-4 py-2 text-left">Label</th>
            <th className="px-4 py-2 text-left">Date</th>
            <th className="px-4 py-2 text-left">Time</th>
            <th className="px-4 py-2 text-left">STATUS</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index} className="border-t border-gray-700">
              <td className="px-4 py-2">{index + 1}</td>
              <td className="px-4 py-2">{item[0]}</td>
              <td className="px-4 py-2">{item[1]}</td>
              <td className="px-4 py-2">{item[2]}</td>
              <td className="px-4 py-2">{item[3]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}