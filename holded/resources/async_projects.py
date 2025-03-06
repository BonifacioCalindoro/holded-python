"""
Asynchronous projects resource for the Holded API.
"""
from typing import Any, Dict, List, Optional, cast

from . import AsyncBaseResource


class AsyncProjectsResource(AsyncBaseResource):
    """
    Resource for interacting with the Projects API asynchronously.
    """

    async def list(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all projects asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of projects
        """
        result = await self.client.get("projects", "projects", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new project asynchronously.

        Args:
            data: Project data

        Returns:
            The created project
        """
        result = await self.client.post("projects", "projects", data)
        return cast(Dict[str, Any], result)

    async def get(self, project_id: str) -> Dict[str, Any]:
        """
        Get a specific project asynchronously.

        Args:
            project_id: The project ID

        Returns:
            The project details
        """
        result = await self.client.get("projects", "projects", project_id)
        return cast(Dict[str, Any], result)

    async def update(self, project_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a project asynchronously.

        Args:
            project_id: The project ID
            data: Updated project data

        Returns:
            The updated project
        """
        result = await self.client.put("projects", "projects", project_id, data)
        return cast(Dict[str, Any], result)

    async def delete(self, project_id: str) -> Dict[str, Any]:
        """
        Delete a project asynchronously.

        Args:
            project_id: The project ID

        Returns:
            The deletion response
        """
        result = await self.client.delete("projects", "projects", project_id)
        return cast(Dict[str, Any], result)

    async def get_summary(self, project_id: str) -> Dict[str, Any]:
        """
        Get a project summary asynchronously.

        Args:
            project_id: The project ID

        Returns:
            The project summary
        """
        result = await self.client.get("projects", f"projects/{project_id}/summary")
        return cast(Dict[str, Any], result)

    async def list_tasks(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all tasks asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of tasks
        """
        result = await self.client.get("projects", "tasks", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_task(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new task asynchronously.

        Args:
            data: Task data

        Returns:
            The created task
        """
        result = await self.client.post("projects", "tasks", data)
        return cast(Dict[str, Any], result)

    async def get_task(self, task_id: str) -> Dict[str, Any]:
        """
        Get a specific task asynchronously.

        Args:
            task_id: The task ID

        Returns:
            The task details
        """
        result = await self.client.get("projects", "tasks", task_id)
        return cast(Dict[str, Any], result)

    async def delete_task(self, task_id: str) -> Dict[str, Any]:
        """
        Delete a task asynchronously.

        Args:
            task_id: The task ID

        Returns:
            The deletion response
        """
        result = await self.client.delete("projects", "tasks", task_id)
        return cast(Dict[str, Any], result)

    async def list_project_time_trackings(self, project_id: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all time trackings for a specific project asynchronously.

        Args:
            project_id: The project ID
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of time trackings for the project
        """
        result = await self.client.get("projects", f"projects/{project_id}/times", params=params)
        return cast(List[Dict[str, Any]], result)

    async def create_project_time_tracking(self, project_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a time tracking for a specific project asynchronously.

        Args:
            project_id: The project ID
            data: Time tracking data

        Returns:
            The created time tracking
        """
        result = await self.client.post("projects", f"projects/{project_id}/times", data)
        return cast(Dict[str, Any], result)

    async def get_project_time_tracking(self, project_id: str, tracking_id: str) -> Dict[str, Any]:
        """
        Get a specific time tracking for a project asynchronously.

        Args:
            project_id: The project ID
            tracking_id: The time tracking ID

        Returns:
            The time tracking details
        """
        result = await self.client.get("projects", f"projects/{project_id}/times/{tracking_id}")
        return cast(Dict[str, Any], result)

    async def update_project_time_tracking(self, project_id: str, tracking_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a time tracking for a project asynchronously.

        Args:
            project_id: The project ID
            tracking_id: The time tracking ID
            data: Updated time tracking data

        Returns:
            The updated time tracking
        """
        result = await self.client.put("projects", f"projects/{project_id}/times/{tracking_id}", data)
        return cast(Dict[str, Any], result)

    async def delete_project_time_tracking(self, project_id: str, tracking_id: str) -> Dict[str, Any]:
        """
        Delete a time tracking for a project asynchronously.

        Args:
            project_id: The project ID
            tracking_id: The time tracking ID

        Returns:
            The deletion response
        """
        result = await self.client.delete("projects", f"projects/{project_id}/times/{tracking_id}")
        return cast(Dict[str, Any], result)

    async def list_all_time_trackings(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        List all time trackings across all projects asynchronously.

        Args:
            params: Optional query parameters (e.g., page, limit)

        Returns:
            A list of all time trackings
        """
        result = await self.client.get("projects", "times", params=params)
        return cast(List[Dict[str, Any]], result) 