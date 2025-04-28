from abc import ABC, abstractmethod
from django.db.models import QuerySet
from .models import BlogPost


class QueryStrategy(ABC):
    """Abstract base class for query strategies."""
    
    @abstractmethod
    def get_queryset(self) -> QuerySet:
        """Get the queryset based on the strategy."""
        pass


class AdminStrategy(QueryStrategy):
    """Strategy for admin users - returns all blog posts."""
    
    def get_queryset(self) -> QuerySet:
        return BlogPost.objects.all()


class AuthorStrategy(QueryStrategy):
    """Strategy for authors - returns their own blog posts."""
    
    def __init__(self, user):
        self.user = user
    
    def get_queryset(self) -> QuerySet:
        return BlogPost.objects.filter(author=self.user)


class PublicStrategy(QueryStrategy):
    """Strategy for public users - returns only published blog posts."""
    
    def get_queryset(self) -> QuerySet:
        return BlogPost.objects.published()


class StaffStrategy(QueryStrategy):
    """Strategy for staff users - returns published and draft blog posts."""
    
    def get_queryset(self) -> QuerySet:
        return BlogPost.objects.filter(status__in=['published', 'draft'])


class QueryStrategyFactory:
    """Factory for creating query strategies based on user roles."""
    
    @staticmethod
    def get_strategy(user):
        """Get the appropriate strategy based on user roles."""
        if user.is_superuser:
            return AdminStrategy()
        elif user.is_staff:
            return StaffStrategy()
        elif user.is_authenticated:
            return AuthorStrategy(user)
        else:
            return PublicStrategy() 